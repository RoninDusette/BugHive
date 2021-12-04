from django.db import models
from BugHive.components.users.models import CustomUser as User


class AudioRecording(models.Model):
    user = models.ForeignKey(User, name="User", max_length=30, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100)
    date_created = models.DateTimeField("Created", auto_now_add=True)
    date_modified = models.DateTimeField("Modified", auto_now=True)
    notes = models.CharField("Notes", max_length=500, null=True, blank=True)
    audio_file = models.FileField("Audio File", upload_to='audio-recordings/')

    def __str__(self):
        return self.audio_file
