from django.urls import path ,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'trainers', views.TrainerViewSet)

urlpatterns = [
    path('signup/', views.trainer_signup, name='trainer_signup'),
    path('signin/', views.trainer_signin, name='trainer_signin'),
     path('logout/<int:id>/', views.trainer_signout, name='signout'),
    path('', include(router.urls)),
]
