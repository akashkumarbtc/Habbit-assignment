from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import RegistrationSerializer
from . import models


@api_view(['POST'])
def registration_view(request):
    """
        registration_view is used to register a new user.
        [Request support: POST
        URI             : register/
        serializer      : RegistrationSerializer]

        A new user can register by posting following JSON data,
        { "username": "username", "email": "email@email.com",
        "password": "password", "password2":"password" }

        On successful registration a token will be send in response
    """

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logout_view(request):
    """
        logout_view is used to logout an user.
        [Request support: POST
        URI             : logout/
        serializer      : - ]

        On logout user token will be deleted from database
    """
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
