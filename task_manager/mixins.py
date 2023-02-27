from django.contrib import messages
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError
from django.utils.translation import gettext as _


class ProtectionCheckMixin:
    error_message = 'Error'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.error_message)
            return redirect('statuses_list')


class PermRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        site_user = self.get_object()
        if request.user != site_user:
            messages.error(request, _('no rights to change'))
            return redirect('user_list')
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, _('Cannot delete user because it is in use'))
            return redirect('user_list')
