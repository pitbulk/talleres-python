from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
from mongoengine.django.auth import User
from nonrel.models import Accion


class UserSerializer(MongoEngineModelSerializer):
    class Meta:
        model = User
        exclude = ('is_superuser','is_active', 'is_staff', 'last_login', 'date_joined', 'user_permissions',)


class AccionSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Accion
        depth = 1
