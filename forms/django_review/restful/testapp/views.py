from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TesterSerializer
from .models import TesterModel

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class TesterViewSet(viewsets.ModelViewSet):
    queryset = TesterModel.objects.all().order_by('name')
    serializer_class = TesterSerializer


class TestingGet(APIView):
    def get(self, request):
        try:
            result: dict = {"result": "success", "message": "타겟의 가장 최신 Task의 결과를 가져오는데 성공했습니다."}
            return Response(result, status=200)
        
        except (KeyError, Http404) as e:
            result = {"result": "error", "message": "Error"}
            return Response(result, status=404)