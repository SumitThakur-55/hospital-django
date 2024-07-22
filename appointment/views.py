from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import *
@login_required(login_url='/login/')
def appointment_view(request):
    appointments = None  
    if  request.method == 'POST':
        data=request.POST
        first_name = data.get('first_name')
        last_name=data.get('last_name')
        email = data.get("email")
        phone_number=data.get('phone_number')
        date_of_appointment = data.get('date_of_appointment')
        doctor=data.get('doctor')
        
        appointments=Appointment.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        date_of_appointment=date_of_appointment,
        doctor=doctor, 
          
        )
        appointments.save()
        return redirect('/appointment')
    return render(request, 'appointment.html',{'Appointment': appointments})
@user_passes_test(lambda user: user.is_superuser, login_url='/doc-login/')
def dashboard_view(request):
    appointments = Appointment.objects.all()

    if request.GET.get('search'):
        appointments =appointments.filter(first_name__icontains=request.GET.get('search'))
    return render(request, 'dashboard.html', {'appointments': appointments})
def delete_appointment(request,id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('/dashboard')
def update_appointment(request, id):
    appointments = get_object_or_404(Appointment, id=id)
    
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get("email")
        phone_number = data.get('phone_number')
        date_of_appointment = data.get('date_of_appointment')
        doctor = data.get('doctor')

        appointments.first_name = first_name
        appointments.last_name = last_name
        appointments.email = email
        appointments.phone_number = phone_number
        appointments.date_of_appointment = date_of_appointment
        appointments.doctor = doctor

        appointments.save()
        return redirect('/dashboard')

    return render(request, 'update_appointment.html', {'appointments': appointments})

    
