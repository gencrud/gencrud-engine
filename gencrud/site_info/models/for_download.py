from django.db import models
from site_info.models import Tag


class ForDownload(models.Model):
    class Meta:
        verbose_name = 'For download'
        verbose_name_plural = 'For downloads'

    UPLOAD_TO = 'uploads/for_download'

    file = models.FileField(upload_to=UPLOAD_TO, verbose_name='File to download')
    # AS function url = models.URLField(verbose_name='Link to download')
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    number_of_downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'File: {self.file}'

    @property
    def link_to_download(self):
        return self.file.url
