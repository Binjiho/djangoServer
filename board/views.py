from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from board.models import SiteEvt
from .serializers import SiteEvtSerializer
# from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from board.models import UserBoard
from .serializers import UserBoardSerializer

@api_view(['GET'])
def getData(request):
    # person = {'name':'frank', 'age': 30}
    board_list = SiteEvt.objects.all().order_by('-no')
    serializer = SiteEvtSerializer(board_list, many=True)
    # return Response(serializer.data)
    return render(request, 'board/board_list.html', context=dict(board_list = board_list))
def detail(request, evt_no):
    evt_detail = get_object_or_404(SiteEvt, pk=evt_no)
    return render(request, 'board/board_list_detail.html', {'blog': evt_detail})


# from .models import UserBoard
# from .serializers import UserBoardSerializer
# modelViewSet
class UserBoardViewSet(ModelViewSet):
    queryset = UserBoard.objects.all().order_by('-no')
    serializer_class = UserBoardSerializer
