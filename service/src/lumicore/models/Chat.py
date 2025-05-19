from django.db import models
from authentication.models import Profile
from simple_history.models import HistoricalRecords

class Chat(models.Model):
  """Modelo Chat para armazenar informações de chat.
  Este modelo é usado para acompanhar sessões de chat e seus usuários associados.
  Atributos:
    - id: Identificador único para a sessão de chat.
    - title: Título da sessão de chat.
    - user: Chave estrangeira para o modelo Profile, representando o usuário associado ao chat.
    - created_at: Data e hora de criação da sessão de chat.
    - updated_at: Data e hora da última atualização da sessão de chat.
  """
  
  history = HistoricalRecords()
  
  id = models.UUIDField("ID", primary_key=True, editable=False)
  
  title = models.CharField("Title", max_length=255)
  
  user = models.ForeignKey(
    Profile,
    on_delete=models.CASCADE,
    related_name="chats",
    verbose_name="User",
  )
  
  created_at = models.DateTimeField("Created At", auto_now_add=True)
  updated_at = models.DateTimeField("Updated At", auto_now=True)
  
  class Meta:
    verbose_name = "Chat"
    verbose_name_plural = "Chats"
    ordering = ["-created_at"]
  
  def __str__(self):
    return self.title
  
  def __repr__(self):
    return f"Chat({self.id}, {self.title})"