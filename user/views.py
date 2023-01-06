# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .controller.registration import RegistrationController
from .models import UsrInfo
from .serializers import UsrInfoSerializer
from common.base.handler.handlers import BaseResponseHandler
from common.base.view.viewsets import AllowEveryOneViewSet, ApiViewSet, AdministratorViewSet, \
    AcademyAdministratorViewSet, ParentsViewSet, StudentViewSet


# modelViewSet
class UsrInfoViewSet(AllowEveryOneViewSet):
    queryset = UsrInfo.objects.all()
    serializer_class = UsrInfoSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            return RegistrationController.login(request)
        except Exception as e:
            return BaseResponseHandler.get_exception_response(e)

