#board/serializers.py
from rest_framework import serializers
from .models import SiteEvt
from .models import UserBoard

class SiteEvtSerializer(serializers.ModelSerializer) :
    class Meta :
        model = SiteEvt        # SiteEvt 모델 사용
        fields = '__all__'            # 모든 필드 포함

class UserBoardSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserBoard
        fields = '__all__'