from django.shortcuts import render
from django.conf import settings
import requests
# Create your views here.
class GetUploadURL(APIView):
    def post(self, request):
        url= f"https://../accounts{settings.CF_ID}/images/v2/"
        one_time_url = requests.post(url, headers={
            "Authorization":f"Bearer {settings.CF_TOCKEN}"
        })
        one_time_url = one_time_url.json()
        return Response(one_time_url)