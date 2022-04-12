from django.contrib import admin

from gen.abstract.admin import (AbstractPageSeoAdmin, AbstractImageInlineAdmin)
from gen.page.strings import APP_NAME
from page.models import (Page, PageImage)


class PageImageInline(AbstractImageInlineAdmin):
    model = PageImage


@admin.register(Page)
class BasePageAdmin(AbstractPageSeoAdmin):
    inlines = (PageImageInline,)
    actions = AbstractPageSeoAdmin.actions + ('set_fixtures', 'load_fixtures')

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BasePageAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = 'Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BasePageAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = 'Фикстуры: Загрузить последние'

