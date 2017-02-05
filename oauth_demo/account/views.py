from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def sign_in(request):
    if request.method == "GET":
        return render_to_response('login.html')
    else:
        # processing signin action

        # authenticate & exception handling

        # status 未定
        return HttpResponse(status=200)



def sign_out(request):
    if request.user.is_authenticated:
        print ("user has been login")
        logout(request)

    return redirect("/")
    

def get_user_info(request):
    if request.user.is_authenticated:
        print (request.user.username, request.user.email)
    else:
        print ("Anoymous user")
    
    return HttpResponse(status=200)
