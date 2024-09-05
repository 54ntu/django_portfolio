from rest_framework import serializers
from .models import Project,Blogs,Comments,Portfolio


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields = ('id','project_name','project_url','tech_used')



