from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime

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

    def update_item_data(self, request, id, partial=False):
        """
        Data update method template.

        Used in methods:
        - put
        - patch

        Patameters:
        - request: A request object containing the new data to update
        - id (int): The ID of the Item object to update
        - partial (bool): Indicates whether the update is partial (True for PATCH) or complete (False for PUT)

        Returns:
        - Respomse: The serilized data of the updated object on success (HTTP 200)
          or a validation error message (HTTP 400)
        """
        instance = self.get_object(id=id)
        serializer = ItemSerializer(instance=instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        item = self.get_object(id=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        return self.update_item_data(request, id, partial=False)

    def patch(self, request, id):
        return self.update_item_data(request, id, partial=True)

    def delete(self, request, id):
        item = self.get_object(id=id)
        item.delete()
        return Response({"delete": f"deleted item by id {id}"}, status=status.HTTP_200_OK)


class MenuItemView(TemplateView):
    """
    A view fro displaying a list of all menu items.

    Methods:
    - get_context_data:
      - Sets the context for the template
      - Adds a list of Item model objects, sorted by creation date in reverse order
      - Returns the context for use in the template
    """
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["items"] = Item.objects.all().order_by("-created_at")
        context["items"] = [
            {
                "item_name": "Butter Chicken",
                "item_price": 350,
                "created_at": datetime(2025, 8, 9, 12, 0, 0),
            },
            {
                "item_name": "Panner Tikka",
                "item_price": 280,
                "created_at": datetime(2025, 1, 20, 8, 0, 0),
            },
        return context


class MenuItemDetailView(TemplateView):
    """
    A view fro displaying derailed information about a single menu item.

    Methods:
    - get_context_data:
      - Gets the context for the template
      - Finds the Item object by the "id" parameter passed in the URL
      - If the ocject exists, adds it to the context as "item"
      - If It does not exist, returns a 404 error
    """
    template_name = "menu-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = self.kwargs.get("id")
        context["item"] = get_object_or_404(Item, id=item_id)
        context["restaurant_name"] = settings.RESTAURANT_NAME
        return context