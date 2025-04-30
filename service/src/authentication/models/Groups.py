from django.contrib.auth.models import Group


class Groups(Group):
    class Meta:
        proxy = True
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    pass
