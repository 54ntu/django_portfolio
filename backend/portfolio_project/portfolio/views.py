from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
from .models  import Blogs,Comments,Portfolio,Project
from .serializers import ProjectModelSerializer

# Create your views here.
class ProjectViewsets(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadOnly]



