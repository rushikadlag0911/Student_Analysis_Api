from functools import wraps

from django.http import JsonResponse
from rest_framework import status


def user_passes_test(data):
    def decorator(func):
        def wrapper(request):
            roll_num = request.data['roll_num']
            if roll_num == None:
                return JsonResponse("some parameter is missing", status=status.HTTP_400_BAD_REQUEST , safe=False)
            if roll_num == " ":
                return JsonResponse("some parameter is missing", status=status.HTTP_400_BAD_REQUEST, safe=False)
            if roll_num not in roll_num:
                return JsonResponse("Roll number is not there", status=status.HTTP_400_BAD_REQUEST, safe=False)

            return func(request)
        return wrapper
    return decorator

