from django.http import HttpResponseForbidden


def user_is_approved(view_func):
    def _wrapped_view(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated and user.is_approved or user.is_superuser:
            return view_func(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not approved to perform this action.")

    return _wrapped_view
