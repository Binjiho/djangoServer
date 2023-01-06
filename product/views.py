from rest_framework.decorators import action
from rest_framework.response import Response
from .controller.salesitem import SalesItemController
from .models import Goods
from .serializers import GoodsSerializer
from common.base.handler.handlers import BaseResponseHandler
from common.base.view.viewsets import AllowEveryOneViewSet, ApiViewSet, AdministratorViewSet, \
    AcademyAdministratorViewSet, ParentsViewSet, StudentViewSet


# modelViewSet
class GoodsViewSet(AllowEveryOneViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # search_fields, ordering_fields -> request
    def list(self, request):
        try:
            search_fields = {

            }
            ordering_fields = {

            }
            result = SalesItemController.list(request=request, search_fields=search_fields,
                                              ordering_fields=ordering_fields)
        except Exception as e:
            return BaseResponseHandler.get_exception_response(e)
        else:
            return Response(result)

    def retrieve(self, request, pk):
        try:
            return SalesItemController.retrieve(request, pk)
        except Exception as e:
            return BaseResponseHandler.get_exception_response(e)

    def create(self, request):
        try:
            return SalesItemController.create(request)
        except Exception as e:
            return BaseResponseHandler.get_exception_response(e)

    def update(self, request, pk):
        try:
            return SalesItemController.update(request, pk)
        except Exception as e:
            return BaseResponseHandler.get_exception_response(e)

    # @action(detail=False, methods=['post'], parser_classes=(MultiPartParser, FileUploadParser))
    # def create_published_book(self, request):
    #     try:
    #         return SalesItemController.create_published_book(request)
    #     except Exception as e:
    #         return BaseResponseHandler.get_exception_response(e)
