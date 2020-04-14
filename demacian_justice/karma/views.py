from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the karma index.")

def v1(request):
    name = request.GET.get('name')
    data = {
        'name': name,
        'is_active': True,
        'karma': 0,
        'count': 28
    }
    return JsonResponse(data)