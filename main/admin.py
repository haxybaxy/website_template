from django.contrib import admin

from .models import (EducationItem, ExperienceDescription, IntroText, Keyword,
                     OpenPositions, Project, ProjectImage, Publication,
                     SiteSettings, Talk, WorkItem, ResearchLine, Course)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "journal", "publication_date")
    search_fields = ("title", "authors", "abstract")
    filter_horizontal = ("keywords",)
    list_filter = ("publication_date", "journal", "keywords")
    date_hierarchy = "publication_date"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "start_year", "end_year")
    search_fields = ("title", "description")
    filter_horizontal = ("keywords",)
    list_filter = ("start_year", "end_year")


@admin.register(OpenPositions)
class OpenPositionsAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(IntroText)
class IntroTextAdmin(admin.ModelAdmin):
    list_display = ("text_preview",)

    def text_preview(self, obj):
        # Return first 50 characters of the text as a preview
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text

    text_preview.short_description = "Text Preview"


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty forms to display


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title", "description")
    filter_horizontal = ("publications",)
    inlines = [
        ProjectImageInline
    ]

@admin.register(ResearchLine)
class ResearchLineAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    filter_horizontal = ("projects", "publications")
    search_fields = ("title", "description")



@admin.register(EducationItem)
class EducationItemAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "date_range", "order")
    list_editable = ("order",)


@admin.register(WorkItem)
class WorkItemAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "date_range", "order")
    list_editable = ("order",)


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    list_display = ("title", "date")


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent creating multiple settings
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the settings
        return False


@admin.register(ExperienceDescription)
class ExperienceDescriptionAdmin(admin.ModelAdmin):
    list_display = ("description",)


class KeywordAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Keyword, KeywordAdmin)
