from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailView(APIView):

    def get_object(self, id):
        """
        Gets and returns the item by its ID or returns an error 404 accepts attribute id.

        Used in methods:
        - update_data
        - get
        """
        return get_object_or_404(Item, id=id)

    def update_data(self, id, partial=False):
        """
        Data update method template, accepts attribute id and partial.

        Used in methods:
        - put
        - patch
        """
        instance = get_object(Item, id=id)
        serializer = ItemSerializer(instance=instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        item = get_object(Item, id=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        update_data(id, partial=False)

    def patch(self, request, id):
        update_data(id, partial=True)

    def delete(self, request, id):
        item = get_object(id)
        item.delete()
        return Response({"delete": f"deleted item by id {id}"}, status=status.HTTP_200_OK)
