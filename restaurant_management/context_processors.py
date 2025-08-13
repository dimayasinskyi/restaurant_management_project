from django.conf import settings


def restaurant_info(request):
    return {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "Restaurant name not provided."),
        "restaurant_phone": getattr(settings, "RESTAURANT_CONTACT_PHONE", "Contact phone number not provided."),
        "restaurant_working_hours": getattr(settings, "WORKING_HOURS", [{"days": "Working hours not provided", "hours": ""}]),
    }