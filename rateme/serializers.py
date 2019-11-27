from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'contacts']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title','description', 'image', 'url', 'pub_date']