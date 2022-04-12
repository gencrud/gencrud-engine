from django.contrib import admin

from gen.abstract.admin import AbstractDefaultMPTTAdmin
from settings_template.models.main_menu import MainMenu


@admin.register(MainMenu)
class BaseMenuAdmin(AbstractDefaultMPTTAdmin):

    radio_fields = {
        'parent': admin.VERTICAL,
        'catalog': admin.VERTICAL,
        'blog': admin.VERTICAL,
        'page': admin.VERTICAL,
    }

    search_fields = ('name', )
    actions = AbstractDefaultMPTTAdmin.actions + ('set_fixtures', 'load_fixtures')
    list_filter = (
        'is_show', 'catalog', 'blog', 'level', 'tree_id'
    )
    list_display = ('name', 'parent', 'is_show', 'catalog', 'page', 'blog', 'sort')
    list_display_links = ('name', 'parent')
    list_editable = ('is_show', 'sort')
