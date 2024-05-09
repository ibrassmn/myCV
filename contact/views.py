from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def contact_form(request):
    context = {
        'success': True,
        'message': 'Contact Form Sent Successfully.'
    }
    return JsonResponse(context)

def contact(request):
    return render(request, 'index.html')