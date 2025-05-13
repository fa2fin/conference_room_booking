from django.http import JsonResponse

def check_availability(request):
    return JsonResponse({'available': True})