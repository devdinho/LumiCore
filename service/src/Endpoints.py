"""

Painel Administrativo:
    - 'admin/' -> URL para acessar a interface do painel de administração.
    - PS: O painel de administração é acessível apenas para usuários autenticados com permissões de administrador.
    - PS2: Todas as URLs do painel de administração começam com 'admin/'.
    - PS3: O painel de administração é protegido por autenticação básica, portanto, você precisará fornecer um nome de usuário e senha válidos para acessá-lo.

Endpoints Autenticação:
    - 'api/register/' -> [POST] Endpoint para registrar um novo usuário.
        ```json
            {
                "first_name": "string",
                "last_name": "string",
                "username": "string",
                "password": "string",
                "email": "string",
            }
        ```
        - Resposta:
        ```json
            {
                "id": "integer",
                "first_name": "string",
                "last_name": "string",
                "username": "string",
                "email": "string",
                "last_login": "string",
                "date_joined": "string",
            }
        ```
    - 'api/login/' -> [POST] Endpoint para obter o token de acesso.
        ```json
            {
                "username": "string",
                "password": "string"
            }
        ```
        - Resposta:
        ```json
            {
                "access": "string",
                "refresh": "string"
            }
        ```
        - PS: O token de acesso é necessário para acessar os endpoints protegidos da API.
    - 'api/login/refresh/' -> [POST] Endpoint para atualizar o token de acesso.
        ```json
            {
                "refresh": "string"
            }
        ```
        - Resposta:
        ```json
            {
                "access": "string"
            }
        ```

    - Logout:
        - Não existe endpoint para fazer logout do usuário.
        - PS: O logout é feito automaticamente quando o token de acesso expira ou é revogado.
        - PS2: O token de acesso é revogado quando o usuário altera sua senha ou exclui sua conta.
        - PS3: O token deve ser excluido do localStorage do navegador.

Endpoints de Profile:
    - 'api/profile/' -> [GET] Endpoint para obter as informações do perfil do usuário autenticado.
    ```json
        headers:{ "Authorization": "string",}
    ```
    - Resposta:
    ```json
        {
            "id": "integer",
            "first_name": "string",
            "last_name": "string",
            "username": "string",
            "email": "string",
            "grower": {
                "id": "string",
                "caf": "string or null",
                "address": "string",
                "level_of_education": "string",
                "document": "string",
                "document_type": "string"
            },
            "last_login": "string or null",
            "date_joined": "string"
        }
    ```

"""
