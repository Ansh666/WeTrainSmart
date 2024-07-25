from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
import random
import re

from .models import Trainer
from .serializers import TrainerSerializer
from api.user.serializers import UserSerializer

# Utility to generate session token
def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice(
        [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    ) for _ in range(length))

# Generalized signin function
def general_trainer_signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only'})

    email = request.POST['email']
    password = request.POST['password']

    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at least 3 characters'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=email)
        trainer = Trainer.objects.get(email=email)

        if trainer.check_password(password):
            if trainer.session_token != "0":
                trainer.session_token = "0"
                trainer.save()
                return JsonResponse({'error': "Previous session exists!"})

            token = generate_session_token()
            trainer.session_token = token
            trainer.save()
            login(request, user)
            return JsonResponse({'token': token, 'trainer': TrainerSerializer(trainer).data})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except (UserModel.DoesNotExist, Trainer.DoesNotExist):
        return JsonResponse({'error': 'Invalid Email'})

@csrf_exempt
def trainer_signup(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only'})

    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']

    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at least 3 characters'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.create_user(email=email, password=password)
        trainer = Trainer.objects.create(email=email, name=name)
        trainer.set_password(password)
        trainer.session_token = generate_session_token()
        trainer.save()
        login(request, user)
        return JsonResponse({'token': trainer.session_token, 'trainer': TrainerSerializer(trainer).data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def trainer_signin(request):
    return general_trainer_signin(request)

@csrf_exempt
def trainer_signout(request, id):
    logout(request)
    # UserModel = get_user_model()
    try:
        trainer = Trainer.objects.get(pk=id)
        trainer.session_token = "0"
        trainer.save()
    except Trainer.DoesNotExist:
        return JsonResponse({'error': 'Invalid trainer ID'})
    return JsonResponse({'success': 'Logout success'})

class TrainerViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = Trainer.objects.all().order_by('id')
    serializer_class = TrainerSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
