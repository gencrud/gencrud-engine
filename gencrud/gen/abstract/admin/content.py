from django.contrib import admin


class BaseContentAdmin:
    _fields = ('title', 'description', 'html', 'is_show', 'author', 'sort', 'tags', 'is_allow_comments')
    filter_horizontal = ('tags',)

    @staticmethod
    def fieldsets_main_content():
        return tuple(('title', 'description', 'html', 'is_show', 'sort', 'is_allow_comments'))


class AbstractContentAdmin(BaseContentAdmin, admin.ModelAdmin):
    class Meta:
        abstract = True
