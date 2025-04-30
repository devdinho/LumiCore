from django.contrib import admin

from authentication.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Admin do modelo de perfil de usuário personalizado.

    Este admin é baseado no modelo de usuário padrão do Django, mas com
    campos adicionais.

    Atributos herdados:
      - username (str): Nome de usuário.
      - first_name (str): Primeiro nome.
      - last_name (str): Último nome.
      - email (str): Endereço de e-mail.
      - is_staff (bool): Indica se este usuário pode acessar este site de administração.
      - is_active (bool): Indica se este usuário deve ser tratado como ativo.
      - date_joined (datetime): Data e hora em que este usuário foi adicionado.

    Atributos adicionais:
      - profileType (str): Tipo de perfil baseado em contants do arquivo
      [contants.ProfileType](../../utils/constants.md#service.src.utils.constants.ProfileType).
      - groups (Group): Grupos de permissões aos quais este usuário pertence.
      - user_permissions (Permission): Permissões específicas para este usuário

    Atributos:
      - list_display (tuple): Campos exibidos na lista de registros.
      - search_fields (tuple): Campos pesquisáveis na lista de registros.
      - list_filter (tuple): Campos filtráveis na lista de registros.
      - ordering (tuple): Campos ordenáveis na lista de registros.
      - filter_horizontal (tuple): Campos com relacionamento muitos-para-muitos.
      - fieldsets (tuple): Grupos de campos exibidos ao editar um registro

    """

    list_display = (
        "username",
        "profileType",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
    )
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("profileType", "is_staff", "is_active")
    ordering = ("username", "-profileType")
    filter_horizontal = ("groups", "user_permissions")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Informações Pessoais", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissões",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    icon_name = "person"


admin.site.register(Profile, ProfileAdmin)
