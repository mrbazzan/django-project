
from django.db import models
from cms.models import CMSPlugin


class GistPluginModel(CMSPlugin):
    gist_user = models.CharField(
        "Github User",
        blank=False,
        default="",
        max_length=32,
        help_text="Supply username of Github user",
    )
    gist_id = models.CharField(
        "Gist ID",
        blank=False,
        default="",
        max_length=32,
        help_text="Supply ID of Gist",
    )
    gist_filename = models.CharField(
        "Gist Filename",
        blank=True,
        default="",
        max_length=250,
        help_text="Optional. Supply a filename",
    )

    def __str__(self):
        return f"{self.gist_user}/{self.gist_id}"
