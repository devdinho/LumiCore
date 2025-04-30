from django.contrib import admin
from django.contrib.auth.models import Group

from authentication.models import Groups


class GroupsAdmin(admin.ModelAdmin):
    """Admin do modelo de grupo de permissões personalizado.

    ###### Ele só está aqui para sobrescrever o modelo padrão de grupo do Django.
    """

    icon_name = "people"

    pass


admin.site.unregister(Group)
admin.site.register(Groups, GroupsAdmin)
