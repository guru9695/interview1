from django.shortcuts import render
from testapp.models import detail
from testapp.serializers import detailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class datalist(APIView):
    """
    List all data, or create a new data.
    """
    def get(self, request, format=None):
        data = detail.order_by('name')
        serializer = detailSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = detailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userupdate(APIView):
    """
    update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return detail.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = detailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)