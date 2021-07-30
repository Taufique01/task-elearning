
from rest_framework.permissions import BasePermission

class IsEducator(BasePermission):
    """
    Allows access only to educator users.
    """

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            if request.user.role == 'educator':
                return True

        return False



class IsLearner(BasePermission):
    """
    Allows access only to learners.
    """

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            if request.user.role == 'learner':
                return True

        return False
