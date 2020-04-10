from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializers.HelloSerializer
	def get(self, request, format=None):
		"""Returns a list of API View Features"""
		api_view_features = [
			'Uses HTTP methods as functions (get, post, put, patch, delete)',
			'API view is similar to traditional Django view',
			'Gives you most control over application logic',
			'Mapped manually to urls'
		]

		return Response({'message': 'Hello User', 'list': api_view_features})


	def post(self, request):
		"""create a hello message with our name"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message' : message})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		"""handle updating an object - Replaces the entire object"""
		return Response({'method': 'PUT'})


	def patch(self, request, pk=None):
		"""Hanldes partial updates of an object - just updates few fields of object"""
		return Response({'method': 'PATCH'})

	def delete(self, request, pk=None):
		"""Delete an object"""
		return Response({'method': 'DELETE'})
