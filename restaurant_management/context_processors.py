from django.conf import setiings


def restaurant_info(request):
    return {
        "restaurant_name": setiings.RESTAURANT_NAME,
        "restaurant_phone": setiings.RESTAURANT_CONTACT_PHONE,
    }