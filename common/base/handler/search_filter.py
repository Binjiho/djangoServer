import operator
import re
from ast import literal_eval
from functools import reduce

from django.db.models import Q

from common.utils.datetime import DateTimeUtils

lookup_prefixes = {
    '^': 'istartswith',  # 조건값이 포함되는 데이터를 모두 가져옵니다.
    '=': 'iexact',
    '@': 'search',
    '$': 'iregex',
    '~': 'range',
    '>': 'gte',  # 필드값 >= 조건값
    '<': 'lte'  # 필드값 <= 조건값
}


class QuerySetSearchAndPaginationHandler:
    """
    QuerySet 필터링 기능 및 페이징 처리 핸들러
    """

    def __init__(self, request, queryset=None, search_fields=None, ordering_fields=None, default_filter=None):
        self.request = request
        self.queryset = queryset
        self.search_fields = search_fields
        self.ordering_fields = ordering_fields
        self.limit = None
        self.offset = None
        self.total_count = None
        self.result_queryset = None
        self.default_filter = default_filter

    def queryset_slicer(self, queryset, limit=None, offset=None):
        """
        type_flag=0 -> Condition does not exists.
        type_flag=1 -> Conditions are exists.
        """
        result = None
        if limit is not None and offset is None:
            result = queryset[:limit]
        elif limit is None and offset is not None:
            result = queryset[offset:]
        elif limit is not None and offset is not None:
            result = queryset[offset:offset + limit]
        else:
            result = queryset

        return result

    def filtered_queryset_for_object(self):
        orm_lookup_dic = {}

        # 기본 필터
        if self.default_filter is not None:
            for filter_column in self.default_filter:
                orm_lookup_dic[filter_column] = self.default_filter[filter_column]

        if self.search_fields is not None:
            for search_field in self.search_fields:
                if isinstance(self.search_fields[search_field], Q):
                    orm_lookup_dic[search_field] = self.search_fields[search_field]
                    continue
                field_name = str(self.search_fields[search_field])
                if re.match("^.+\[\]$", search_field) is None:
                    search_term = self.request.query_params.get(search_field, '')
                    if search_term != '':
                        if '[' in search_term or ']' in search_term:
                            orm_lookup_dic[field_name] = literal_eval(search_term)
                        elif re.search("__in$", field_name) is not None:
                            orm_lookup_dic[field_name] = [search_term]
                        else:
                            orm_lookup_dic[field_name] = search_term
                else:
                    search_term = self.request.query_params.getlist(search_field, [])
                    if len(search_term) > 0:
                        orm_lookup_dic[field_name] = search_term

        orm_lookup_ordering_dic = []
        if self.ordering_fields is not None:
            field_name = self.request.query_params.get('sort', '')
            search_term = search_term_by_ordering_field(field_name, self.ordering_fields)
            if len(search_term) > 0:
                orm_lookup_ordering_dic = search_term

        if bool(orm_lookup_ordering_dic) is False and self.ordering_fields is not None:
            search_term = self.ordering_fields.get('default', None)
            if search_term is not None:
                orm_lookup_ordering_dic = search_term

        if not bool(orm_lookup_dic) and not bool(orm_lookup_ordering_dic):
            self.total_count = self.queryset.count()
            self.result_queryset = self.queryset
            # return result_queryset
            return self

        qs = self.queryset
        if bool(orm_lookup_dic):
            # 유효한 검색필터 and 조건으로 모두 충족하는지 검사
            conditions = []
            for key in orm_lookup_dic:
                if isinstance(orm_lookup_dic[key], Q):
                    conditions.append(orm_lookup_dic[key])
                else:
                    conditions.append(reduce(operator.or_, [Q(**{key: orm_lookup_dic[key]})]))

            qs = qs.filter(reduce(operator.and_, conditions))

        self.total_count = qs.count()

        if bool(orm_lookup_ordering_dic):
            qs = qs.order_by(*orm_lookup_ordering_dic)

        self.result_queryset = qs

        return self

    def filtered_queryset_for_object_with_paginated(self):
        limit = self.request.GET.get('limit', None)
        if limit is not None:
            limit = int(limit)
            self.limit = limit

        offset = self.request.GET.get('offset', None)
        if offset is not None:
            offset = int(offset)
            self.offset = offset

        self.filtered_queryset_for_object()
        qs = self.result_queryset
        self.result_queryset = self.queryset_slicer(queryset=qs,
                                                    limit=limit,
                                                    offset=offset)

        return self


def construct_search(field_name):
    lookup = lookup_prefixes.get(field_name[0])
    if lookup:
        field_name = field_name[1:]
    else:
        lookup = 'icontains'
    return '__'.join([field_name, lookup])


def param_name(param):
    if param == '<created_at':
        return 'search_end_date'
    if param == '>created_at':
        return 'search_start_date'
    lookup = lookup_prefixes.get(param[0])
    if lookup:
        return param[1:]
    else:
        return param


def search_term_formatter(term, param):
    if term:
        if param == 'search_start_date':
            return DateTimeUtils.date_string_to_korea_datetime_type_start(term)
        if param == 'search_end_date':
            return DateTimeUtils.date_string_to_korea_datetime_type_end(term)
    else:
        return ''
    return term


def search_term_by_search_field(query_params, search_param):
    param = param_name(search_param)
    return search_term_formatter(query_params.get(param, ''), param)


def search_term_by_ordering_field(field_name, ordering_param):
    return ordering_param.get(field_name, [])


# 날짜 검색: 생성일 필드: created_at
# 검색 파라미터 - 검색 시작일: search_start_date, 검색 종료일: search_end_date
def filtered_queryset(request, queryset, view):
    search_fields = getattr(view, 'search_fields', None)

    orm_lookup_dic = {}
    for search_field in search_fields:
        field_name = construct_search(str(search_field))
        search_term = search_term_by_search_field(request.query_params, search_field)
        if search_term != '':
            orm_lookup_dic[field_name] = search_term

    if not bool(orm_lookup_dic):
        return queryset

    # 유효한 검색필터 and 조건으로 모두 충족하는지 검사
    conditions = []
    for key in orm_lookup_dic:
        conditions.append(reduce(operator.or_, [Q(**{key: orm_lookup_dic[key]})]))

    # print('conditions', conditions)
    queryset = queryset.filter(reduce(operator.and_, conditions))
    return queryset


# 날짜 검색: 생성일 필드: created_at
# 검색 파라미터 - 검색 시작일: search_start_date, 검색 종료일: search_end_date
def filtered_queryset_for_object(request, queryset, search_fields=None, ordering_fields=None):
    orm_lookup_dic = {}
    if search_fields is not None:
        for search_field in search_fields:
            field_name = str(search_fields[search_field])
            if re.match("^.+\[\]$", search_field) is None:
                search_term = request.query_params.get(search_field, '')
                if search_term != '':
                    orm_lookup_dic[field_name] = search_term
            else:
                search_term = request.query_params.getlist(search_field, [])
                if len(search_term) > 0:
                    orm_lookup_dic[field_name] = search_term

    orm_lookup_ordering_dic = []
    if ordering_fields is not None:
        field_name = request.query_params.get('sort', '')
        search_term = search_term_by_ordering_field(field_name, ordering_fields)
        if len(search_term) > 0:
            orm_lookup_ordering_dic = search_term

    if not bool(orm_lookup_dic) and not bool(orm_lookup_ordering_dic):
        return queryset

    if bool(orm_lookup_dic):
        # 유효한 검색필터 and 조건으로 모두 충족하는지 검사
        conditions = []
        for key in orm_lookup_dic:
            conditions.append(reduce(operator.or_, [Q(**{key: orm_lookup_dic[key]})]))

        # print('conditions', conditions)
        queryset = queryset.filter(reduce(operator.and_, conditions))

    if bool(orm_lookup_ordering_dic):
        queryset = queryset.order_by(*orm_lookup_ordering_dic)
    return queryset
