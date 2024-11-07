from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST.get('user_id')  # Using .get() to avoid errors
        
        contact = Contact(
            name=name,
            company=company,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id  # Optional, depending on whether you need this
        )
        contact.save()  # Save the instance to the database

        messages.success(request, 'Your request has been submitted, we will get back to you soon!')
        return redirect('index')
    
    return render(request, 'contacts/contact.html')  # Adjust with your template path
