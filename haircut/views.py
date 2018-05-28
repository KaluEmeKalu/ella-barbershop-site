from django.shortcuts import render
from .models import Appointment
def home_page(request):
    if request.method == 'POST':
        time = request.POST.get('time')
        customer_name = request.POST.get("customer_name")
        barber_name = request.POST.get('barber_name')
        
        appointment_obj = Appointment.objects.create(
            time = time,
            customer_name = customer_name,
            barber_name = barber_name 
        )
        all_appointments = Appointment.objects.all()
        context = {'appointments': all_appointments}
        return render(request, 'haircut/home_page.html', context)
    if request.method == "GET":
        all_appointments = Appointment.objects.all()
        context = {'appointments': all_appointments}
        return render(request, 'haircut/home_page.html', context)
