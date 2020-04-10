from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
	"""Test API View"""

	def get(self, request, format=None):
		"""Returns a list of API View Features"""
		api_view_features = [
			'Uses HTTP methods as functions (get, post, put, patch, delete)',
			'API view is similar to traditional Django view',
			'Gives you most control over application logic',
			'Mapped manually to urls'
		]

		return Response({'message': 'Hello User', 'list': api_view_features})
