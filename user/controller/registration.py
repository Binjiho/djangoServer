from django.db import transaction
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from common.base.controller.controllers import BaseController
from common.base.handler.handlers import BaseResponseHandler
from common.utils.datetime import DateTimeUtils
from user.models import UsrInfo

from user.exception.auth import IsNotCertifiedUserException, UserDoesNotExistException, PasswordNotMatchingException
from common.utils.token import HESMKToken
from django.db import models


class UsrStatus(models.TextChoices):
    # ENUM
    IS_ACTIVE = '20'  # 활동


class RegistrationController(BaseController):

    @classmethod
    def login(cls, request):
        json_data = super().get_json_data(request,
                                          required_attribute=['usr_id', 'password'])
        usr_id = json_data.get('usr_id', None)
        password = json_data.get('password', None)
        # user = UsrInfo.objects.login(usr_id, password)
        user = cls.validate_login(usr_id, password)
        data = BaseResponseHandler.get_common_success_response('로그인에 성공했습니다')
        return cls.get_login_response(data, user)
        # return RegistrationController.get_login_response(data, user)

    @classmethod
    def validate_login(cls, usr_id, password):
        try:
            # 현재 user 변수에는 <QuerySet [<UsrInfo: frank3@bravecompany.io>]> 담겨있음
            # user 변수에 객체로 사용할때 filter().first() or get()
            user = UsrInfo.objects.select_related('usrdtl').get(usr_id=usr_id, state=UsrStatus.IS_ACTIVE)

            if not user.check_password(password):
                raise PasswordNotMatchingException()
            # elif not user.is_certified:
            #     raise IsNotCertifiedUserException()
            else:
                user.last_login = DateTimeUtils.get_now_date()
                user.save()
                return user
        except Exception as e:
            raise e
            # raise UserDoesNotExistException()

    @classmethod
    def get_login_response(cls, data, user):
        token = cls.get_tokens_for_user(user)
        user_state = user.state
        user_etc1 = user.usrdtl.etc1
        # token에 필요한 user 정보 저장해 놓음
        data['user_state'] = user_state
        data['user_etc1'] = user_etc1
        data['refresh_token'] = token['refresh']
        data['access_token'] = token['access']
        # serializer = LoginResponseSerializer(data)
        # return Response(serializer.data)
        return Response(data)

    @classmethod
    def get_tokens_for_user(cls, user):
        refresh = HESMKToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
