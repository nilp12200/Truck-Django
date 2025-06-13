from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import PlantMaster

from django.shortcuts import render, redirect
from django.contrib import messages  # <-- Required for flash messages
from .models import PlantMaster




from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Or use the correct route name
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
     
@login_required
def home(request):
    return render(request, 'home.html')



def staff(request):
    return render(request, 'staff.html')

def gatekeeper(request):
    return render(request, 'gatekeeper.html')

def truck_transaction(request):
    return render(request, 'truck_transaction.html')


def plant_master(request):
    if request.method == 'POST':
        plant_name = request.POST.get('plantName')
        plant_address = request.POST.get('plantAddress')
        contact_person = request.POST.get('contactPerson')
        mobile_no = request.POST.get('mobileNo')
        remarks = request.POST.get('remarks')

        PlantMaster.objects.create(
            plant_name=plant_name,
            plant_address=plant_address,
            contact_person=contact_person,
            mobile_no=mobile_no,
            remarks=remarks
        )

        messages.success(request, "✅ Plant Master data saved successfully.")
        return redirect('plantmaster')  # reload the form or redirect as needed

    return render(request, 'plantmaster.html')