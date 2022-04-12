from django.contrib import admin
from gen.abstract.admin import (AbstractPageSeoAdmin, AbstractImageInlineAdmin)
from home.models import (Home, HomeImage)
from gen.home.strings import APP_NAME


class HomeImageInline(AbstractImageInlineAdmin):
    model = HomeImage
    classes = ('collapse', 'open')


@admin.register(Home)
class BaseHomeAdmin(AbstractPageSeoAdmin):
    inlines = [HomeImageInline, ]
    actions = AbstractPageSeoAdmin.actions + ('set_fixtures', 'load_fixtures')
    raw_id_fields = AbstractPageSeoAdmin.raw_id_fields + ('blog',)
    list_filter = AbstractPageSeoAdmin.list_filter + ('blog', 'tags')
    filter_horizontal = ('catalogs', 'tags')

    fieldsets = (
        ('Main content', {
            'fields': ('title', 'description', 'html', 'video', 'is_show',  'sort', 'is_allow_comments')
        }),
        ('Inner elements', {
            'classes': ('collapse', 'hide'),
            'fields': ('blog', 'catalogs', 'tags')
        }),
        ('SEO options', {
            'classes': ('collapse', 'open'),
            'fields': ('slug', 'seo_title', 'seo_description', 'seo_keywords', 'og_locale'),
        }),
        ('Scripts options', {
            'classes': ('collapse', 'open'),
            'fields': ('scripts', ),
        }),
        ('Information', {
            'classes': ('collapse', 'open'),
            'fields': ('thumb', 'created', 'updated'),
        })
    )

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseHomeAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = '[не применять] Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseHomeAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = '[не применять] Фикстуры: Загрузить последние'



