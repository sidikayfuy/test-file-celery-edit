import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class File(models.Model):
    file = models.FileField(_('file'))
    uploaded_at = models.DateTimeField(_('uploaded at'), default=timezone.now)
    processed = models.BooleanField(_('processed'), default=False)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.filename()

