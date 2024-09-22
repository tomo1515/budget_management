from django.contrib import admin
from .models import RecordDisplay

@admin.register(RecordDisplay)
class RecordDisplayAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
