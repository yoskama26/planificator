from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            #permet d'enregistrer l'utilisateurs dans la database (.save)           
            return redirect('organisation:project')
    else:    
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html',{'form':form})