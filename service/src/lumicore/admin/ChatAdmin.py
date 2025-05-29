from django.contrib import admin
from lumicore.models import Chat

class ChatAdmin(admin.ModelAdmin):
    """Interface de administração para o modelo Chat."""
    
    list_display = ("id", "title", "user", "created_at", "updated_at")
    search_fields = ("title", "user__username")
    ordering = ("-created_at",)
    
admin.site.register(Chat, ChatAdmin)