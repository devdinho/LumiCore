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

class ChatMessageRole(object):
    """Object representando diferentes papéis de mensagens de chat.

    Atributos:
        - USER (int): Usuário, mensagem enviada por um usuário.
        - ASSISTANT (int): Assistente, mensagem enviada pelo assistente.
        - SYSTEM (int): Sistema, mensagem enviada pelo sistema.
    """

    USER = 1
    ASSISTANT = 2
    SYSTEM = 3

    CHAT_MESSAGE_ROLE_CHOICES = (
        (USER, "user"),
        (ASSISTANT, "assistant"),
        (SYSTEM, "system"),
    )

class Prompts(object):
    """Object representando diferentes prompts de chat.

    Atributos:
        - GEN_CHAT_TITLE (str): Prompt de chat, usado para criar um titulo para uma conversa.
    """
    INITIAL_SYSTEM_MESSAGE = "Você é um assistente de chat que ajuda os usuários a encontrar informações e responder perguntas. Por favor, responda às perguntas dos usuários de forma clara e concisa."
    GEN_CHAT_TITLE = "Me responda com uma string, sem dois pontos ou \\, somente o titulo puro e curto para o seguinte início de conversa:"

    PROMPT_CHOICES = (
        (INITIAL_SYSTEM_MESSAGE, "Mensagem inicial do sistema"),
        (GEN_CHAT_TITLE, "Gerar título do chat"),
    )