from django.contrib import admin

from gen.abstract.admin.page import COLLIDE_CLASSES_CSS
from gen.abstract.admin import (AbstractPageSeoAdmin, AbstractImageInlineAdmin)
from home.models import (Home, HomeImage)
from gen.home.strings import APP_NAME


class HomeImageInline(AbstractImageInlineAdmin):
    model = HomeImage
    classes = COLLIDE_CLASSES_CSS


@admin.register(Home)
class BaseHomeAdmin(AbstractPageSeoAdmin):
    inlines = [HomeImageInline, ]
    actions = AbstractPageSeoAdmin.actions + ('set_fixtures', 'load_fixtures')
    raw_id_fields = AbstractPageSeoAdmin.raw_id_fields + ('blog',)
    list_filter = AbstractPageSeoAdmin.list_filter + ('blog', 'tags')
    filter_horizontal = ('catalogs', 'tags')

    fieldsets = (
        ('Main content', {
            'fields': AbstractPageSeoAdmin.fieldsets_main_content() + ('video', )
        }),
        ('Inner elements', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': ('blog', 'catalogs') + ('tags', )
        }),
        ('SEO options', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': AbstractPageSeoAdmin.fieldsets_seo_options()
        }),
        ('Scripts options', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': ('scripts', ),
        }),
        ('Information', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': ('thumb', 'created', 'updated'),
        })
    )

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseHomeAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = '[не применять] Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseHomeAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = '[не применять] Фикстуры: Загрузить последние'



