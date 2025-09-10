from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer, RegisterUserSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        print(f"[DEBUG] request.user: {user}, is_authenticated: {user.is_authenticated}")
        return Task.objects.filter(owner=user).order_by("-created_at")

    def perform_create(self, serializer):
        print(f"[DEBUG] Saving task for user: {self.request.user}")
        serializer.save(owner=self.request.user)

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]
