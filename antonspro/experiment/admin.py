from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.InGroup

class JudgeInline(admin.TabularInline):
    model = models.IsJudge


admin.site.register(models.EGroup)
