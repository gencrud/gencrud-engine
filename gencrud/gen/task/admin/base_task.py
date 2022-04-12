from django.contrib import admin
from gen.abstract.admin import AbstractMPTTPageSeoAdmin, AbstractImageInlineAdmin
from task.models.task import Task
from task.models.task_image import TaskImage


class TaskImageInline(AbstractImageInlineAdmin):
    model = TaskImage


@admin.register(Task)
class BaseTaskAdmin(AbstractMPTTPageSeoAdmin):
    inlines = (TaskImageInline,)
