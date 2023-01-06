#user/serializers.py
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response

from .models import UsrInfo


class UsrInfoSerializer(serializers.ModelSerializer):
    class Meta :
        model = UsrInfo        # UsrInfo 모델 사용
        fields = '__all__'

    # def validate_password(self, value:str) -> str:
    #     return make_password(value)
