from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following',on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers',on_delete=models.CASCADE)
    follow_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('follower','following')
        
    def __str__(self):
        return f"{self.follower.username} ->{self.following.username} (Approved: {self.approved})"


