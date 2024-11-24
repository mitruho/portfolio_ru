from django.contrib import admin
from .models import Project,ContactSubmission
admin.site.register(Project)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('contact_email', 'project_title', 'submitted_at')
    search_fields = ('contact_email', 'project_title')
    list_filter = ('submitted_at',)
