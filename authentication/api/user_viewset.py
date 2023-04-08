from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from authentication.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'last_login', 'username', 'first_name', 'last_name', 'name', 'email', 'password', 'type_user',
            'groups', 'user_permissions')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'success': True}, status=status.HTTP_201_CREATED, headers=headers)
