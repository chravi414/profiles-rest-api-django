from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	"""checks whether user can update the object or not"""
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.id == obj.id

class UpdateOwnFeed(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.id == obj.user_profile.id