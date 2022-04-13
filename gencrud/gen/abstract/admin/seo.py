from django.contrib import admin


class BaseSEOAdmin:
    view_on_site = True
    prepopulated_fields = {'slug': ('title',)}
    actions = ('fill_seo_fields',)
    _fields = ('slug', 'seo_title', 'seo_description', 'seo_keywords', 'og_locale', 'scripts')

    @staticmethod
    def fieldsets_seo_options():
        return tuple(('slug', 'seo_title', 'seo_description', 'seo_keywords', 'og_locale'))

    def fill_seo_fields(self, request, queryset):
        for query in queryset:
            default_title = query.title
            if not query.seo_title:
                query.seo_title = default_title
            if not query.seo_description:
                query.seo_description = default_title
            if not query.seo_keywords:
                query.seo_keywords = default_title
            query.save()

    fill_seo_fields.short_description = 'Заполнить пустые CEO-поля'


class AbstractSEOAdmin(BaseSEOAdmin, admin.ModelAdmin):
    pass
