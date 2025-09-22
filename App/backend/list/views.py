from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas as tarefas do usuário autenticado
        return Task.objects.filter(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def toggle_completed(self, request, pk=None):
        """Endpoint para alternar o status de conclusão de uma tarefa"""
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Endpoint para registro de novos usuários"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user_data = UserSerializer(user).data
        return Response({
            'message': 'Usuário criado com sucesso!',
            'user': user_data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile(request):
    """Endpoint para obter perfil do usuário autenticado"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

from django.http import HttpResponse

def index(request):
    return HttpResponse("API do app List funcionando 🚀")

