from django.contrib import admin
from gen.abstract.admin import AbstractPageSeoAdmin, AbstractImageInlineAdmin
from blog.models import Post, PostImage


class PostImageInline(AbstractImageInlineAdmin):
    model = PostImage


@admin.register(Post)
class BasePostAdmin(AbstractPageSeoAdmin):
    inlines = (PostImageInline,)

    raw_id_fields = ('blog',) + AbstractPageSeoAdmin.raw_id_fields
    readonly_fields = AbstractPageSeoAdmin.readonly_fields + ('comment_count',)
    list_filter = ('blog',) + AbstractPageSeoAdmin.list_filter
    list_display = ('blog',) + AbstractPageSeoAdmin.list_display
    list_display_links = AbstractPageSeoAdmin.list_display_links

