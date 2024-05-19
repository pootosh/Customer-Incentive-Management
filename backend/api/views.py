
import random
from django.shortcuts import render
from rest_framework.views import APIView
from .models import IncentiveCalculations, HolidayPackage, User
from .serializers import IncentiveCalculationsSerializers, HolidayPackageSerializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View


def Generate_token(length=10):
    lst = [chr(i) for i in range(97,123)] + [str(i) for i in range(10)]
    token = "".join(random.SystemRandom().choice(lst) for _ in range(10))
    return token


@csrf_exempt
def Login(request):
    if request.method == 'POST':
        try:
            username = request.headers['username']
            user = User.objects.get(username=username)
            if user.password != request.headers['password']:
                return JsonResponse({'success': False, 'msg': 'Invalid password'})
            else:
                token = Generate_token()
                user.token = token
                user.save()
            return JsonResponse({'success': True, 'token': token})
        except:
            return JsonResponse({'success': False, 'msg': 'Invalid username'})
    
@csrf_exempt
def Authenticate(request):
    try:
        username = request.headers['username']
        token = request.headers['token']
        user = User.objects.get(username=username)
        if user.token != token:
            return JsonResponse({'success': False, 'msg': 'session expired'})
        else:
            return JsonResponse({'success': True, 'msg': 'logged in'})
    except:
        return JsonResponse({'success': False, 'msg': 'logged out'})
        



@csrf_exempt
def Incentive(request):
    if request.method == 'GET':
        incentive = IncentiveCalculations.objects.all()
        
        return JsonResponse({'data': list(incentive.values())})
    elif request.method == 'POST':
        return JsonResponse({'method': 'POST'})
    
@csrf_exempt
def Holiday(request):
    if request.method == 'GET':
        holiday = HolidayPackage.objects.all()
        return JsonResponse({'holiday': list(holiday.values())})