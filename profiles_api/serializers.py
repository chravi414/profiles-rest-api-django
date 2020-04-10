from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	"""Defines a serializer for API View"""
	name = serializers.CharField(max_length=10)
