from rest_framework import status, viewsets
from rest_framework.exceptions import (MethodNotAllowed, NotFound,
                                       PermissionDenied)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.models import Profile
from authentication.serializers import ProfileSerializer


class ProfileRestView(viewsets.ModelViewSet):
    """Endpoint para registrar um novo usuário.

    Payload:
    ```json
        {
            "first_name": "string",
            "last_name": "string",
            "username": "string",
            "password": "string",
            "email": "string",
        }
    ```
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.none()

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST", detail="Create not allowed")

    def list(self, request):
        data = Profile.objects.filter(id=request.user.id)
        if data:
            profile = ProfileSerializer(instance=data, many=True).data[0]
        else:
            raise NotFound(detail="Profile not found")

        return Response(profile, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = Profile.objects.get_object_or_404(id=kwargs.get("pk"))

        if instance.id != request.user.id and not request.user.is_superuser:
            raise PermissionDenied(detail="You can only update your own profile!")

        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE", detail="Delete not allowed")
