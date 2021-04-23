from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Disposition
from .serializers import DispositionSerializer

from django.http import Http404

# Create your views here.
class ListDisposition(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        dispositiones = Disposition.objects.all()
        dispositiones_json = DispositionSerializer(dispositiones, many=True)
        return Response(dispositiones_json.data)

    def post(self, request):
        dispositiones_json = DispositionSerializer(data=request.data)
        if dispositiones_json.is_valid():
            dispositiones_json.save()
            return Response(dispositiones_json.data, status=201)
        return Response(dispositiones_json.errors, status=400)


class DetailDisposition(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Disposition.objects.get(pk=pk)
        except Disposition.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        disposition = self.get_object(pk)
        disposition_json = DispositionSerializer(disposition)
        return Response(disposition_json.data)

    def put(self, request, pk):
        disposition = self.get_object(pk)
        disposition_json = DispositionSerializer(disposition, data=request.data)
        if disposition_json.is_valid():
            disposition_json.save()
            return Response(disposition_json.data)
        return Response(disposition_json.errors, status=400)

    def delete(self, request, pk):
        disposition = self.get_object(pk)
        disposition.delete()
        return Response(status=204)
