from django.https import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'info': 'Django','name': 'Ayush', })