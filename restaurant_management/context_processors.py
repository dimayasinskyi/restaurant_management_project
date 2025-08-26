from django.conf import settings

from home.models import RestaurantLocationModel


def restaurant_info(request):
    return {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "Restaurant name not provided."),
        "restaurant_working_hours": getattr(settings, "WORKING_HOURS", [{"days": "Working hours not provided", "hours": ""}]),
        "restaurant_location_model": RestaurantLocationModel.objects.all(),
    }