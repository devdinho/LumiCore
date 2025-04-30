class ProfileType(object):
    """Object representando diferentes tipos de Perfis de Usuários.

    Atributos:
        - ADMIN (int): Administrador, usuário com permissões de Administrador.
        - DEVELOPER (int): Desenvolvedor, usuário com permissões de Desenvolvedor.
        - EARUSER (int): Usuário Padrão, usuário com permissões de Usuário Padrão.
    """

    ADMIN = 1
    DEVELOPER = 2
    EARUSER = 3

    PROFILE_TYPE_CHOICES = (
        (ADMIN, "Administrador"),
        (DEVELOPER, "Desenvolvedor"),
        (EARUSER, "Usuário Padrão"),
    )

class Status(object):
    """Object representando diferentes status de objetos.

    Atributos:
        - ACTIVE (int): Ativo, objeto ativo.
        - INACTIVE (int): Inativo, objeto inativo.
    """

    ACTIVE = 1
    INACTIVE = 2

    STATUS_CHOICES = (
        (ACTIVE, "Ativo"),
        (INACTIVE, "Inativo"),
    )