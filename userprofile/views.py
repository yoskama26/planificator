from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #récupere le form pour créer un utilisateurs 
        if form.is_valid():
        #vérifie si les données sont correct
            user = form.save() 
            login(request, user)
            #permet d'enregistrer l'utilisateurs dans la database (.save)           
            return redirect('/organisation/project') 
    else:    
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST': #permet d'acceder a la fonction si la request est une push request(POST du coup)
        form = AuthenticationForm(data=request.POST)#recupere le form d'authent de base Django
        if form.is_valid(): #verifie si les données entrer dans les champs correspondant et sont correct (si le username et le mdp est valide) 
            user = form.get_user() #permet de récuperer le "user" qui essaye de se connecter (pour savoir qui il est)
            login(request, user)#permet de log user (si il est valide mais techniquement il le sera toujours grâce au if form.is_valid au dessus)
            if 'next' in request.POST: #permet de voir sur l'url si "next est présent"
                return redirect(request.POST.get('next')) #permet de renvoyer l'utilisateur la ou il s'est connecté
            else:
                return redirect('/organisation/project')#sinon le renvoi sur le projet.
    else:
        form = AuthenticationForm()
    return render(request,'userprofile/login.html',{'form':form})
<<<<<<< HEAD

=======
>>>>>>> 5e536d99f59af565bdf7bdc17eeebd73ab2b13ff
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        pass
<<<<<<< HEAD

=======
>>>>>>> 5e536d99f59af565bdf7bdc17eeebd73ab2b13ff
