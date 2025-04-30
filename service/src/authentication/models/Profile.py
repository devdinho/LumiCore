from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from simple_history.models import HistoricalRecords

from utils.constants import ProfileType


class Profile(AbstractUser):
    """Modelo de perfil de usuário personalizado.

    O perfil de usuário é baseado no modelo de usuário padrão do Django, mas com
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
    """

    history = HistoricalRecords()

    profileType = models.IntegerField(
        "Tipo de Perfil",
        choices=ProfileType.PROFILE_TYPE_CHOICES,
        default=ProfileType.EARUSER,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name="Grupos de Permissões",
        blank=True,
        help_text="Os grupos aos quais este usuário pertence.",
        related_name="usuario_set",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="Permissões de Usuários",
        blank=True,
        help_text="Permissões específicas para este usuário.",
        related_name="usuario_permissions",
        related_query_name="usuario",
    )

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
