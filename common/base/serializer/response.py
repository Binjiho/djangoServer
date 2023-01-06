from django.db import models
from rest_framework import serializers


class SearchDateType(models.TextChoices):
    YEAR = 'year'  # 연도별
    MONTH = 'month'  # 월별
    DATE = 'date'  # 일별


class BaseApiResponse(object):
    def __init__(self, result_flag, message, code, external_data=None):
        self.result = result_flag
        self.message = message
        self.code = code
        self.external_data = external_data

    def get_response_dict(self):
        return {'result': self.result, 'message': self.message, 'code': self.code, 'external_data': self.external_data}


class ResponseSerializer(serializers.Serializer):
    result = serializers.BooleanField()
    message = serializers.CharField()
    code = serializers.CharField(min_length=4, max_length=4)
    external_data = serializers.JSONField()


class BasePaginatedApiResponse(BaseApiResponse):
    def __init__(self, result_flag, message, code, external_data=None, page=None, count=None,
                 page_size=None, page_len=None):
        super().__init__(result_flag, message, code, external_data)
        self.page = page
        self.count = count
        self.page_size = page_size
        self.page_len = page_len

    def get_response_dict(self):
        return {'result': self.result, 'message': self.message, 'code': self.code, 'external_data': self.external_data,
                'page': self.page, 'count': self.count, 'page_size': self.page_size, 'page_len': self.page_len}


class PaginatedResponseSerializer(ResponseSerializer):
    page = serializers.IntegerField()
    page_size = serializers.IntegerField()
    page_len = serializers.IntegerField()
    count = serializers.IntegerField()


class PaginatedLimitOffsetResponseSerializer(ResponseSerializer):
    limit = serializers.IntegerField()
    offset = serializers.IntegerField()
    count = serializers.IntegerField()