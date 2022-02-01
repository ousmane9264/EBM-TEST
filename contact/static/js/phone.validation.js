
$(window).on("load", function() {
    window.intlTelInputGlobals.loadUtils("https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/16.0.8/js/utils.js");
    
    // let tel = document.querySelector(".phone_reference")
    // const iti = intlTelInput(tel, {
    //     initialCountry: 'gn',
    //     separateDialCode: true,
    //     autoPlaceholder: 'polite',
    //     nationalMode: false,
    //     formatOnDisplay: false,
    //     customPlaceholder: function(selectedCountryPlaceholder, selectedCountryData) {
    //         return "Ex: " + selectedCountryPlaceholder;
    //     },
    // })

    // if (tel.value !== '') {
    //     tel.value = tel.value.replace(/\s/g, '')
    // }

 })

// On every :input focusout validate if empty
$(':input').blur(function(){
    let fieldType = this.type;
    switch(fieldType){
        case 'tel':
            validateTelephone($(this), iti);
            break;
        case 'password':
            validatePassword($(this));
            break;
        default:
            break;
    }
});
// Validate telephone
function validateTelephone(thisObj, iti) {
    let fieldValue = thisObj.val();
    let tele = document.querySelector("#user_telephone")
    if (fieldValue !== '') {
        thisObj.val(fieldValue.replace(/\s/g, ''))
        
        if (thisObj.val()[0] === "+" && thisObj.val().slice(1,4) === '224') {
            thisObj.val(thisObj.val().slice(4))
        } 
    
        if (thisObj.val().slice(0,3) !== "610") {
            if(iti.isValidNumber()) {
                thisObj.addClass('is-valid')
                $('#tel-inv-feedback').hide()
                $("#user_code_pays").val(iti.getSelectedCountryData().dialCode)
                tele.setCustomValidity('')
            } else {
                thisObj.addClass('is-invalid')
                $('#tel-inv-feedback').show()
                $("#user_code_pays").val('')
                tele.setCustomValidity('Invalid!')
            }
        }else{
            const old_number = thisObj.val()
            thisObj.val(`620${thisObj.val().slice(3)}`)
            if(iti.isValidNumber()) {
                thisObj.addClass('is-valid')
                thisObj.val(old_number) 
                $('#tel-inv-feedback').hide()
                $("#user_code_pays").val(iti.getSelectedCountryData().dialCode)
                tele.setCustomValidity('')
            } else {
                thisObj.addClass('is-invalid')
                thisObj.val(old_number)
                $('#tel-inv-feedback').show()
                $("#user_code_pays").val('')
                tele.setCustomValidity('Invalid!')
            }
        }

    } else {
        thisObj.addClass('is-invalid')
        $('#tel-inv-feedback').show()
        tele.setCustomValidity('Invalid!')
    }
}