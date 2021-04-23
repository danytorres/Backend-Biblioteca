from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Affair
from .serializers import AffairSerializer

from django.http import Http404

# Create your views here.
class ListAffair(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        affairs = Affair.objects.all()
        affair_json = AffairSerializer(affairs, many=True)
        return Response(affair_json.data)

    def post(self, request):
        affair_json = AffairSerializer(data=request.data)
        if affair_json.is_valid():
            affair_json.save()
            return Response(affair_json.data, status=201)
        return Response(affair_json.errors, status=400)


class DetailAffair(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Affair.objects.get(pk=pk)
        except Affair.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        affair = self.get_object(pk)
        affair_json = AffairSerializer(affair)
        return Response(affair_json.data)

    def put(self, request, pk):
        affair = self.get_object(pk)
        affair_json = AffairSerializer(affair, data=request.data)
        if affair_json.is_valid():
            affair_json.save()
            return Response(affair_json.data)
        return Response(affair_json.errors, status=400)

    def delete(self, request, pk):
        affair = self.get_object(pk)
        affair.delete()
        return Response(status=204)
