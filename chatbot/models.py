from django.db import models
from users.models import CustomUser

class ChatMessage(models.Model):
    #user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE)
    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return f"User: {self.user_message}, Bot: {self.bot_response}"
    
    

