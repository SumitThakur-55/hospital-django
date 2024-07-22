from .models import Doc
from django.contrib.auth.backends import BaseBackend

class DocBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Doc.objects.get(username=username)

            # Check the password here
            if user.password == password:
                return user
        except Doc.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Doc.objects.get(pk=user_id)
        except Doc.DoesNotExist:
            return None
