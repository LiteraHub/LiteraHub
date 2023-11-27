# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt  
def register(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    repassword = data['repassword']
    print(username)

    if(password==repassword):
        try:
            user= User.objects.create_user(username=username,password=password)
            if(user!=None):
                user.save()
                return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Your account has been successfully created!"
            }, status=200)
        except:
                return JsonResponse({
                "status": False,
                "message": "Registration Failed. The name has already been used."
                }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Registration Failed. Check your password."
        }, status=401)