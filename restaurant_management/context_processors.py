from django.conf import settings


def restaurant_info(request):
    return {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_phone": settings.RESTAURANT_CONTACT_PHONE,
        "restaurant_working_hours": settings.WORKING_HOURS,
    }