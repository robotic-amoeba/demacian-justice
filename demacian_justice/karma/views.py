from django.http import HttpResponse, JsonResponse
from .client import Client

def index(request):
    return HttpResponse("Hello, world. You're at the karma index.")

def get_summoner(request):
    summoner_name = request.GET.get('summoner_name')
    client = Client()
    response = client.get_summoner(summoner_name)
    return JsonResponse(response.json(), status=response.status_code)