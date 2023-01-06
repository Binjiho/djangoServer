from rest_framework.response import Response

from common.base.exception.exceptions import DefaultException, DoesNotExistException
from common.base.serializer.response import BaseApiResponse, ResponseSerializer, \
    BasePaginatedApiResponse


class BaseResponseHandler:
    @classmethod
    def get_server_exception_response(cls, exception):
        if isinstance(exception, DefaultException):
            return Response(status=exception.status, exception=True)
        else:
            return Response(status=500, exception=True)

    @classmethod
    def get_exception_response(cls, exception):
        if isinstance(exception, DefaultException):
            data = BaseApiResponse(False, str(exception), exception.code)
            serializer = ResponseSerializer(data)
            return Response(serializer.data)
        else:
            data = BaseApiResponse(False, str(exception), "FAIL")
            serializer = ResponseSerializer(data)
            return Response(serializer.data)

    @classmethod
    def get_common_success_response(cls, success_message=None):
        if success_message is None:
            success_message = "성공"
        data = BaseApiResponse(True, success_message, 'GOOD')
        return data.get_response_dict()

    @classmethod
    def get_success_service_response(cls, response_serializer, additional_data_dict=None, success_message=None):
        data = BaseResponseHandler.get_common_success_response(success_message)
        if additional_data_dict is not None :
            for key, value in additional_data_dict.items():
                data[key] = value
        serializer = response_serializer(data)
        return Response(serializer.data)

    @classmethod
    def get_paginated_success_response(cls, success_message=None):
        if success_message is None:
            success_message = "성공"
        data = BasePaginatedApiResponse(True, success_message, 'GOOD')
        return data.get_response_dict()

