from django.db import models

class Video(models.Model):
    matn = models.TextField(max_length=2200)
    # rasm = models.ImageField(upload_to='rasm/', null=True, blank=True)
    # audio = models.FileField(upload_to='audio/', null=True, blank=True)
    # musiqa = models.FileField(upload_to='musiqa/', null=True, blank=True)
    # fayl = models.FileField(upload_to='fayl/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

