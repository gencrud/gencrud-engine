from django.contrib import admin
from site_info.models import ForDownload


@admin.register(ForDownload)
class ForDownloadAdmin(admin.ModelAdmin):
    readonly_fields = ('link_to_download', )
    list_display = ('__str__', 'tag', 'link_to_download', 'number_of_downloads', 'updated')
    list_filter = ('tag', 'updated')
