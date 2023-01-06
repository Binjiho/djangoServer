from django.shortcuts import render
from rest_framework.views import APIView
from board.models import SiteEvt


class Main(APIView):
    def get(self, request):
        return render(request, 'djangoProject/login.html')
    def post(self, request):
        site_evt_list = SiteEvt.objects.all()
        return render(request, 'djangoProject/main.html', context=dict(site_evt_list = site_evt_list))