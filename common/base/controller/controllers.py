import enum
import json


from common.base.exception.exceptions import ParameterException
from ast import literal_eval


class BaseController(object):
    MULTIPART_FORM_LIST_SEPARATOR = ','

    @classmethod
    def get_json_data(cls, request, required_attribute=None):
        required_attribute
        if required_attribute is None:
            required_attribute = list()
        try:
            json_data = json.loads(request.body)
            for attribute in required_attribute:
                if json_data.get(attribute, None) is None:
                    print(attribute)
                    raise ParameterException()
            return json_data
        except Exception as e:
            print(e)
            raise ParameterException()

    @classmethod
    def request_to_dict(cls, request, request_method_type: enum.Enum = None, required_attribute: list = None):
        if required_attribute is None:
            required_attribute = list()

        try:
            if request_method_type.value == 0 or request_method_type.value == 2:
                data_dict = request.query_params
            elif request_method_type.value == 1 or request_method_type.value == 3:
                data_dict = json.loads(request.body)

            for attribute in required_attribute:
                if data_dict.get(attribute, None) is None:
                    print(attribute)
                    raise ParameterException("필수 파라미터 {}(이/가) 누락되었습니다".format(attribute))

            return data_dict
        except Exception as e:
            print(e)
            raise e
