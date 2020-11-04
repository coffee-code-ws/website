from django.db import models
from django.utils.crypto import get_random_string


def generate_token_value():
    return get_random_string(length=64)


"""
A token used for the continuous integration authentication.
"""
class GitloadToken(models.Model):
    value = models.TextField(
        default=generate_token_value,
        editable=False,
        primary_key=True
    )

    def __str__(self):
        return self.value
