from django.conf import setiings


def restaaurant_info(request):
    return {
        "restaurant_name": setiings.RESTAURANT_NAME
    }