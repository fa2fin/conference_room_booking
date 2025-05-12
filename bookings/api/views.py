from django.http import JsonResponse

def check_availability(request):
    # Заглушка для теста
    return JsonResponse({'available': True})