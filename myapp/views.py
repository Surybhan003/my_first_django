from django.shortcuts import render, redirect
from .forms import ContactFormModelForm

def contact_view(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect after successful submission
    else:
        form = ContactFormModelForm()
    return render(request, 'myapp/contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')
