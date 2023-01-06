import json

from rest_framework.viewsets import ViewSet

from common.base.exception.exceptions import ParameterException
from common.permissions import AllowEveryOnePermission, IsAuthenticated, IsStudent, IsParents, IsAdministrator, \
    IsAcademyAdministrator, IsTeacher, IsAssistant, IsSoftBridge


class BaseViewSet(ViewSet):
    @classmethod
    def get_json_data(cls, request, required_attribute=None):
        if required_attribute is None:
            required_attribute = list()
        try:
            json_data = json.loads(request.body)
            for attribute in required_attribute:
                if json_data.get(attribute, None) is None:
                    raise ParameterException()
            return json_data
        except Exception as e:
            raise ParameterException()


class AllowEveryOneViewSet(BaseViewSet):
    authentication_classes = []
    permission_classes = [AllowEveryOnePermission]


class AllowEveryOneMixedViewSet(BaseViewSet):
    permission_classes = [AllowEveryOnePermission | IsAuthenticated]


class ApiViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]


class StudentViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & IsStudent]


class ParentsViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & IsParents]


class AdministratorViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & IsAdministrator]


class AcademyAdministratorViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & IsAcademyAdministrator]


class AdAaViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & (IsAdministrator | IsAcademyAdministrator)]


class LecturerViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & IsTeacher]


class LMSControllerViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & (IsTeacher | IsAssistant)]


class SoftBridgeViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated & IsSoftBridge]
