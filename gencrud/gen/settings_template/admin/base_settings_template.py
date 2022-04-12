from django.contrib import admin
from settings_template.models.settings_template import SettingsTemplate
from gen.abstract.admin import AbstractDefaultAdmin, AbstractImageAdmin
from gen.settings_template.strings import APP_NAME


@admin.register(SettingsTemplate)
class BaseSettingsTemplateAdmin(AbstractDefaultAdmin, AbstractImageAdmin):
    search_fields = ('name', 'parent')
    actions = AbstractDefaultAdmin.actions + AbstractImageAdmin.actions + ('set_fixtures', 'load_fixtures')
    list_filter = ('is_included', 'home', 'footer')
    list_display = ('title', 'thumb', 'email', 'phone', 'address', 'is_included')
    list_display_links = ('title', 'thumb',)
    list_editable = ('is_included',)

    def clone_object(self, request, queryset): pass
    clone_object.short_description = 'Клонировать: недоступно!'

    def set_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseSettingsTemplateAdmin, self).set_fixtures(request, queryset, dir_name)
    set_fixtures.short_description = 'Фикстуры: Сохранить текущие'

    def load_fixtures(self, request, queryset, dir_name=APP_NAME, filename='default.json'):
        super(BaseSettingsTemplateAdmin, self).load_fixtures(request, queryset, dir_name)
    load_fixtures.short_description = 'Фикстуры: Загрузить последние'

