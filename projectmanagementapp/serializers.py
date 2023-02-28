from .models import Project
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our Projecterializer
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Project
        # the fields that should be included in the serialized output
        fields = ['id', 'title', 'owner', 'deadline', 'description', 'tags', 'content', 'created_at', 'updated_at']