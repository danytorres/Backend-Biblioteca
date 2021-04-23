from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from .serializers import CreateUserSerializer

from decouple import config


CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
SERVER = config("SERVER")


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    """
    Registra al usuario en el servidor. La entrada debe estar en el formato:
    {"username": "username", "password": "1234abcd"}
    """
    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        r = requests.post(
            f"{SERVER}/o/token/",
            data={
                "grant_type": "password",
                "username": request.data["username"],
                "password": request.data["password"],
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
        res = r.json()
        res["user"] = {"username": request.data["username"]}
        return Response(res)
    return Response(serializer.errors)


@api_view(["POST"])
@permission_classes([AllowAny])
def token(request):
    """
    Obtiene tokens con nombre de usuario y contraseña. La entrada debe estar en el formato:
    {"username": "username", "password": "1234abcd"}
    """
    r = requests.post(
        f"{SERVER}/o/token/",
        data={
            "grant_type": "password",
            "username": request.data["username"],
            "password": request.data["password"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    res = r.json()
    res["user"] = {"username": request.data["username"]}
    return Response(res)


@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registra al usuario en el servidor. La entrada debe estar en el formato:
    {"refresh_token": "<token>"}
    """
    r = requests.post(
        f"{SERVER}/o/token/",
        data={
            "grant_type": "refresh_token",
            "refresh_token": request.data["refresh_token"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(["POST"])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Método para revocar tokens.
    {"token": "<token>"}
    """
    r = requests.post(
        f"{SERVER}/o/revoke_token/",
        data={
            "token": request.data["token"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    if r.status_code == requests.codes["ok"]:
        return Response({"message": "token revoked"}, r.status_code)

    return Response(r.json(), r.status_code)
