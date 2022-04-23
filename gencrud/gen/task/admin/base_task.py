from django.contrib import admin

from gen.abstract.admin import AbstractMPTTPageSeoAdmin, AbstractImageInlineAdmin
from task.models.task import Task
from task.models.task_image import TaskImage


class TaskImageInline(AbstractImageInlineAdmin):
    model = TaskImage


@admin.register(Task)
class BaseTaskAdmin(AbstractMPTTPageSeoAdmin):
    inlines = (TaskImageInline,)
    fieldsets = (
        ('Main content', {
            'fields': tuple(
                ('title', 'description', 'html', 'document', 'is_show', 'sort', 'is_allow_comments')
            )
        }),

        AbstractMPTTPageSeoAdmin.fieldsets[1],
        AbstractMPTTPageSeoAdmin.fieldsets[2],
        AbstractMPTTPageSeoAdmin.fieldsets[3],
        AbstractMPTTPageSeoAdmin.fieldsets[4]
    )
