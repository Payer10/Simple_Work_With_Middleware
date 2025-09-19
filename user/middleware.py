from django.shortcuts import redirect,HttpResponse
from django.conf import settings

class AuthRequiredMiddleware:
    """
    Custom middleware that redirects users to the login page
    if they are not authenticated.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow these paths without authentication
        allowed_paths = [
            settings.LOGIN_URL,  # e.g. '/login/'
            '/admin/login/',
        ]

        # If user is not authenticated and trying to access a protected page
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect(settings.LOGIN_URL)
        return HttpResponse('the user access middleware is successful.')

        response = self.get_response(request)
        return response
