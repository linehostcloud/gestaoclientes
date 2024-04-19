from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
