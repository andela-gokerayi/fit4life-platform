"""
Users views.py.
"""
from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics
# # from rest_framework.response import Response
# from rest_framework.reverse import reverse


class UserList(generics.ListCreateAPIView):
    """
    User's List Class.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    User's Details Class.
    """

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)
    