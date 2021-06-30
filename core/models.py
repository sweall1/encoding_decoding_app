from django.db import models


class Encoder(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Decoder(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
