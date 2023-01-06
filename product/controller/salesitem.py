import gc

from rest_framework.response import Response

from common.base.controller.controllers import BaseController
from common.base.exception.exceptions import ParameterException
from common.base.handler.handlers import BaseResponseHandler
from common.base.handler.search_filter import QuerySetSearchAndPaginationHandler
from product.exception.salesitem import SalesItemDoesNotExistException
from product.models import Goods
from product.serializers import GoodsListResponseSerializer, GoodsItemResponseSerializer


class SalesItemController(BaseController):
    # BRAVECOMPANY_IMPORT_API_KEY = "5943535325853664"
    # BRAVECOMPANY_IMPORT_API_SECRET = "13eb4f20e5aa0e251013110fd4e4300fa75c9c0ba2d16b0cf2a23091d9189a51e5a7623f20fdf2f5"
    # IMPORT_TOKEN_URL = "https://api.iamport.kr/users/getToken"
    # IMPORT_GET_PURCHASE_URL = "https://api.iamport.kr/payments/"
    # IMPORT_CANCEL_URL = "https://api.iamport.kr/payments/cancel"

    @classmethod
    def retrieve(cls, request, pk=None):
        if pk is None:
            raise ParameterException()
        else:
            try:
                # sales_item = Goods.objects.select_related('program').get(pk=pk)
                sales_item = Goods.objects.get(pk=pk)
                data = BaseResponseHandler.get_common_success_response('판매 상품을 불러왔습니다')
                data['sales_item'] = sales_item
                serializer = GoodsItemResponseSerializer(data)

                # 메모리 해제
                del sales_item
                del data
                gc.collect()
                # 왜 상세에서는 response로 return 하나
                return Response(serializer.data)
            except Goods.DoesNotExist:
                raise SalesItemDoesNotExistException()

    @classmethod
    def list(cls, request, academy=None, search_fields=None, ordering_fields=None, default_filter=None):
        try:
            # query_set = Goods.objects.select_related('program') \
            #     .prefetch_related(
            #     'program__origin_program__academy__logo',
            #     'program__origin_program__grade_set',
            #     'program__origin_program__subject',
            #     'program__origin_program__lecturer__subject',
            #     'program__origin_program__lecturer__academy_set',
            #     # 'program__origin_program__lecturer__publishedprogram_set',
            #     'program__origin_program__lecturer__program_set',
            #     'program__introduction_image',
            #     'program__introduction_vod',
            #     'program__introduction_vod_thumb',
            #     'program__publishedbook_set',
            #     'program__publishedlecture_set__publishedlecturecontents_set__vod_info') \
            #     .filter(is_active=True)

            query_set = Goods.objects.all()
            if default_filter is None:
                default_filter = {}

            # if academy is not None:
            #     default_filter['program__origin_program__academy_id'] = academy.id

            handler = QuerySetSearchAndPaginationHandler(request=request, queryset=query_set,
                                                         search_fields=search_fields,
                                                         ordering_fields=ordering_fields, default_filter=default_filter)

            goods_items = handler.filtered_queryset_for_object_with_paginated()

            data = BaseResponseHandler.get_common_success_response('상품 리스트를 불러왔습니다')
            data['limit'] = goods_items.limit
            data['offset'] = goods_items.offset
            data['sales_item_list'] = goods_items.result_queryset
            data['count'] = goods_items.total_count

            # dict 타입
            serializer = GoodsListResponseSerializer(data)
            # 메모리 해제
            del query_set
            del handler
            del data
            gc.collect()

            result = serializer.data
        except Exception as e:
            raise e
        else:
            return result
