from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import random
import re

# Utility to generate session token
def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice(
        [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    ) for _ in range(length))

# Generalized signin function
def general_signin(request, user_role=None):
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

        if user.check_password(password):
            if user_role and user.role != user_role:
                return JsonResponse({'error': f'This endpoint is for {user_role}s only'})

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': "Previous session exists!"})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': UserSerializer(user).data})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})

@csrf_exempt
def signup(request):
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
        user = UserModel.objects.create_user(name=name, email=email, password=password)
        user.session_token = generate_session_token()
        user.save()
        login(request, user)
        return JsonResponse({'token': user.session_token, 'user': UserSerializer(user).data})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
@csrf_exempt
def signin(request):
    return general_signin(request)

@csrf_exempt
def trainer_signin(request):
    return general_signin(request, user_role=CustomUser.Role.TRAINER)

@csrf_exempt
def signout(request, id):
    logout(request)
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})
    return JsonResponse({'success': 'Logout success'})

class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
