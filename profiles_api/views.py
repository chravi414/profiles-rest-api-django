from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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



class HelloViewSet(viewsets.ViewSet):
	"""Test API view set"""

	serializer_class= serializers.HelloSerializer

	def list(sefl, request):
		"""Return a hello message"""

		view_set_feature = [
			'User actions (list, create, retrive, update, partial updates)',
			'Automatically maps urls using routers',
			'Provides more functionality using less code'
		]

		return Response({'message': 'hello', 'list': view_set_feature}) 

	def create(self, request):
		"""Creates a new hello message"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message': message})
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


	def retrieve(self, request, pk=None):
		"""Retrieves the particaular object"""
		return Response({'method': 'Retrieve/GET'})

	def update(self, request, pk=None):
		"""Updates the particluar object"""
		return Response({'method': 'Update/PUT'})

	def partial_update(self, request, pk=None):
		"""Updates the particluar object"""
		return Response({'method': 'Partial Update/PATCH'})

	def destroy(self, request, pk=None):
		"""Deletes the particluar object"""
		return Response({'method': 'Destroy/DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handle creating and updating the Users"""
	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email')
 

class UserLoginApiView(ObtainAuthToken):
 	"""Handle creating user Auth tokens"""
 	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedView(viewsets.ModelViewSet):
	serializer_class = serializers.UserProfileFeedSerializer
	queryset = models.UserProfileFeedItem.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated, permissions.UpdateOwnFeed,)

	def perform_create(self, serializer):
		serializer.save(user_profile=self.request.user)