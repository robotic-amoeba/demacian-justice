from django.db import models
from django.utils import timezone

class Summoner(models.Model):
    name = models.CharField(max_length=50)
    puuid = models.CharField(max_length=100, unique=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    UPVOTE_FIELD = "upvote"
    DOWVOTE_FIELD = "downvote"

    def vote(self, vote):
        if vote == Summoner.UPVOTE_FIELD:
            self.upvotes += 1
        elif vote == Summoner.DOWVOTE_FIELD:
            self.downvotes += 1
        self.save
        return self


