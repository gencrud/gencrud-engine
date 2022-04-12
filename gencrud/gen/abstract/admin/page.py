from mptt.admin import MPTTModelAdmin
from .default import AbstractDefaultAdmin
from .created import AbstractCreatedAdmin
from .seo import AbstractSEOAdmin
from .content import AbstractContentAdmin
from .image import AbstractImageAdmin
from gen.abstract.forms import HTMLFieldAdminForm


class AbstractPageSeoAdmin(AbstractDefaultAdmin, AbstractContentAdmin, AbstractSEOAdmin,
                           AbstractImageAdmin, AbstractCreatedAdmin):
    class Meta:
        abstract = True

    form = HTMLFieldAdminForm
    search_fields = ('title',)
    readonly_fields = AbstractImageAdmin.readonly_fields + AbstractCreatedAdmin.readonly_fields
    raw_id_fields = ('author',)
    list_filter = ('is_show', 'is_allow_comments',  'tags', 'created', 'updated')
    list_display = ('thumb', 'title', 'slug', 'is_show', 'is_allow_comments', 'sort', 'created')  # 'get_html'
    list_display_links = ('thumb', 'title',)
    list_editable = ('sort', 'is_show', 'is_allow_comments')


class AbstractMPTTPageSeoAdmin(MPTTModelAdmin, AbstractPageSeoAdmin):
    class Meta:
        abstract = True

    mptt_level_indent = 23
    actions = ('rebuild',) + AbstractPageSeoAdmin.actions
    raw_id_fields = ('parent',) + AbstractPageSeoAdmin.raw_id_fields
    list_filter = ('parent',) + AbstractPageSeoAdmin.list_filter
    list_display = ('parent',) + AbstractPageSeoAdmin.list_display
    list_display_links = ('parent',) + AbstractPageSeoAdmin.list_display_links

    def rebuild(self, request, queryset):
        self.model.objects.rebuild()
    rebuild.short_description = 'Пересобрать пункты раздела'
