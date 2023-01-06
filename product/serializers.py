from rest_framework import serializers
from common.base.serializer.response import PaginatedLimitOffsetResponseSerializer, ResponseSerializer
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class SalesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['sal_cd', 'sal_nm', 'sal_mng_nm', 'prod_knd_cd', 'sal_amt', 'sal_thum', 'sal_sdt', 'sal_edt', 'state']


class GoodsItemResponseSerializer(ResponseSerializer):
    sales_item = SalesItemSerializer(many=False, read_only=True)


class SalesItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['sal_cd', 'sal_nm', 'sal_mng_nm', 'prod_knd_cd', 'sal_amt', 'sal_thum', 'sal_sdt', 'sal_edt', 'state']


class GoodsListResponseSerializer(PaginatedLimitOffsetResponseSerializer):
    # serializer는 한개의 객체만 이해할 수 있고 리스트는 이해할 수 없다. objects.all() 검색한 객체는 리스트이므로 many = True사용
    sales_item_list = SalesItemListSerializer(many=True, read_only=True)
