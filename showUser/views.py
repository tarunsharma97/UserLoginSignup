from django.shortcuts import render, redirect
import pyrebase
 
 
config={
    'apiKey': "AIzaSyAsjifnT3YGdOyj6qru1lwGwcQR2CIjV9s",
    'authDomain': "userloginsystem-f9140.firebaseapp.com",
    'projectId': "userloginsystem-f9140",
    'storageBucket': "userloginsystem-f9140.appspot.com",
    'messagingSenderId': "666753482813",
    'appId': "1:666753482813:web:30893dc7737092eac96a54",
    'databaseURL': "",
    'measurementId': "G-ZHF2433MTM"
}
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"home.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        return redirect('/')
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return redirect('home')
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect('/')
 
def signUp(request):
    return render(request,"Register.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "Register.html")
     return redirect('/')

def resetpass(request):
    return render(request, "password_reset.html")

def postresetpass(request):
    email = request.POST.get('email')
    link = authe.generate_password_reset_link(email, action_code_settings)
    send_custom_email(email, link)
    return render(request, "password_reset.html")