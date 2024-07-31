from django.shortcuts import render
from . forms import GeeksforgeeksForm, OrdinaryCodersForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def geeksforgeeks_form(request):
    formData = GeeksforgeeksForm()
    if request.method == 'POST':
        formData = GeeksforgeeksForm(request.POST, request.FILES)
        if formData.is_valid():
            # file = formData.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            return render(request, 'geeksforgeeks.html', {'form' : formData})
    
    return render(request, 'geeksforgeeks.html', {'form' : formData})

def ordinaryCoders_form(request):
    formData = OrdinaryCodersForm()
    if request.method == 'POST':
        formData = OrdinaryCodersForm(request.POST, request.FILES)
        return render(request, 'ordinarycoders.html', {'form' : formData})
    
    return render(request, 'ordinarycoders.html', {'form' : formData})
        