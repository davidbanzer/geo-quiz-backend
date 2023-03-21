from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_logged = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        login(request, user)
        response = super(LoginAPI, self).post(request, format=None)
        response.data['user'] = user_logged
        return response