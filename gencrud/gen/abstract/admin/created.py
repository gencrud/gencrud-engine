from django.contrib import admin


class BaseCreatedAdmin:
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')
    list_filter = ('created', 'updated')


class AbstractCreatedAdmin(BaseCreatedAdmin, admin.ModelAdmin):
    class Meta:
        abstract = True
