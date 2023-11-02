from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("first_name", "last_name")
    serializer_class = UserSerializer
    search_fields = ["first_name", "last_name", "profile__gov_id"]
