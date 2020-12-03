from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # send an email

        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['meharifitex1@gmail.com'],  # to email
        )

        context = {
            'message_name': message_name,
        }
        return render(request, "contact.html", context)
    else:
        context = {}
        return render(request, "contact.html", context)


def home(request):
    context = {}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def services(request):
    context = {}
    return render(request, "services.html", context)


def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        department = request.POST['department']
        doctor = request.POST['doctor']
        message = request.POST['message']

        # send an email
        your_message = 'your name:' + name + 'your phone:' + phone + ' date:' + date + ' department:' + department + ' doctor:' + doctor + ' message:' + message
        send_mail(
            your_message,  # message
            email,  # from email
            ['meharifitex1@gmail.com', ],  # to email
        )

        context = {'name': name,
                   'email': email,
                   'phone': phone,
                   'date': date,
                   'department': department,
                   'doctor': doctor,
                   'message': message}
        return render(request, "appointment.html", context)
    else:
        context = {}
        return render(request, "home.html", context)
