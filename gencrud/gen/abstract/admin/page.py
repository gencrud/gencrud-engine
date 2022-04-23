from .default import AbstractDefaultAdmin, AbstractDefaultMPTTAdmin
from .created import AbstractCreatedAdmin, BaseCreatedAdmin
from .seo import AbstractSEOAdmin, BaseSEOAdmin
from .content import AbstractContentAdmin, BaseContentAdmin
from .image import AbstractImageAdmin, BaseImageAdmin
from gen.abstract.forms import HTMLFieldAdminForm

COLLIDE_CLASSES_CSS = ('collapse', 'open')


class AbstractPageSeoAdmin(AbstractDefaultAdmin, BaseContentAdmin, BaseSEOAdmin, BaseImageAdmin, BaseCreatedAdmin):
    class Meta:
        abstract = True

    view_on_site = True
    prepopulated_fields = {'slug': ('title',)}

    form = HTMLFieldAdminForm
    search_fields = ('title',)
    readonly_fields = AbstractImageAdmin.readonly_fields + AbstractCreatedAdmin.readonly_fields
    raw_id_fields = ('author',)
    list_filter = ('is_show', 'is_allow_comments',  'tags', 'created', 'updated')
    list_display = ('thumb', 'title', 'slug', 'is_show', 'is_allow_comments', 'sort')  # 'get_html'
    list_display_links = ('thumb', 'title',)
    list_editable = ('sort', 'is_show', 'is_allow_comments')
    filter_horizontal = ('tags', )

    fieldsets = (
        ('Main content', {
            'fields': AbstractContentAdmin.fieldsets_main_content()
        }),
        ('Inner elements', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': ('tags', )
        }),
        ('SEO options', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': AbstractSEOAdmin.fieldsets_seo_options()
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


class AbstractMPTTPageSeoAdmin(AbstractDefaultMPTTAdmin, BaseContentAdmin, BaseSEOAdmin, BaseImageAdmin, BaseCreatedAdmin):
    class Meta:
        abstract = True

    mptt_level_indent = 23

    view_on_site = True
    prepopulated_fields = {'slug': ('title',)}

    form = HTMLFieldAdminForm
    search_fields = AbstractPageSeoAdmin.search_fields
    actions = ('rebuild',) + AbstractPageSeoAdmin.actions
    readonly_fields = AbstractPageSeoAdmin.readonly_fields
    raw_id_fields = ('parent',) + AbstractPageSeoAdmin.raw_id_fields
    list_filter = ('parent',) + AbstractPageSeoAdmin.list_filter
    list_display = ('parent',) + AbstractPageSeoAdmin.list_display
    list_display_links = ('parent',) + AbstractPageSeoAdmin.list_display_links
    list_editable = AbstractPageSeoAdmin.list_editable
    filter_horizontal = AbstractPageSeoAdmin.filter_horizontal
    fieldsets = (
        AbstractPageSeoAdmin.fieldsets[0],
        ('Inner elements', {
            'classes': COLLIDE_CLASSES_CSS,
            'fields': ('parent', 'tags')
        }),
        AbstractPageSeoAdmin.fieldsets[2],
        AbstractPageSeoAdmin.fieldsets[3],
        AbstractPageSeoAdmin.fieldsets[4]
    )

    def rebuild(self, request, queryset):
        self.model.objects.rebuild()
    rebuild.short_description = 'Пересобрать пункты раздела'
