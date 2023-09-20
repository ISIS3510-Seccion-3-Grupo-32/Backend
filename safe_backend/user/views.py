from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('mail')
            password = data.get('password')

            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Usuario logueado correctamente'}, status=200)
            else:
                return JsonResponse({'error': 'El usuario no se encuentra registrado'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato de datos equivocado'}, status=400)
    else:
        return JsonResponse({'error': "Se esperaba una solicitud POSR"}, status=400)
    
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('mail')
            password = data.get('password')
            date_of_birth = data.get('date_of_birth')

            user = CustomUser.objects.create_user(name=name, email=email, password=password, date_of_birth=date_of_birth)
            user.save()
            return JsonResponse({'message': 'Usuario creado correctamente'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato de datos equivocado'}, status=400)
        
def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'Usuario deslogueado correctamente'}, status=200)

    

