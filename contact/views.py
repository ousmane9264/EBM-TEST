from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Form
# Create your views here.
def index(request):
    return render(request, 'contact.html')

def send_data(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            niveau_etude = form.cleaned_data['niveau_etude']
            centre_souhaite = form.cleaned_data['centre_souhaite']
            formation_souhaitee = form.cleaned_data['formation_souhaitee']

            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'contact.html', {'form': form})
