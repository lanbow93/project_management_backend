from .models import Project
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProjectSerializer


class TodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Project.objects.all()
    # The serializer class for serializing output
    serializer_class = ProjectSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
