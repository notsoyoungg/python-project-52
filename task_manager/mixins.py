from django.contrib import messages
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin


class ProtectionCheckMixin:
    error_message = 'Error'
    error_url = 'index'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.error_message)
            return redirect(self.error_url)


class ModifiedUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request, _('No rights to change another user'))
            return redirect('user_list')
