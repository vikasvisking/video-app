from rest_framework import serializers
from .models import Videos

class VideoSerializers(serializers.ModelSerializer):
	""" This Serializer For Videos """

	class Meta:
		model = Videos
		fields = "__all__"