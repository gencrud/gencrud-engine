from django.contrib import admin


class AbstractContentAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    _fields = ('title', 'description', 'html', 'is_show', 'author', 'sort', 'tags', 'is_allow_comments')
    filter_horizontal = ('tags',)
