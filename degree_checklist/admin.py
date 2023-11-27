from django.contrib import admin
from django import forms
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment

# Register models
admin.site.register(Student)
admin.site.register(DegreeProgram)
admin.site.register(Course)
admin.site.register(DegreeChecklistTemplate)
admin.site.register(StudentDegreeChecklist)
admin.site.register(CourseEnrollment)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset):
        # data import logic for the Student model here
        # This function will be called when the "Import Data" action is selected in the admin interface

    import_data.short_description = "Import Data"


@admin.register(DegreeProgram)
class DegreeProgramAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset):
        # data import logic for the DegreeProgram model here
        # This function will be called when the "Import Data" action is selected in the admin interface

    import_data.short_description = "Import Data"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset):
        # data import logic for the Course model here
        # This function will be called when the "Import Data" action is selected in the admin interface

    import_data.short_description = "Import Data"


@admin.register(DegreeChecklistTemplate)
class DegreeChecklistTemplateAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset):
        # data import logic for the DegreeChecklistTemplate model here
        # This function will be called when the "Import Data" action is selected in the admin interface

    import_data.short_description = "Import Data"


@admin.register(StudentDegreeChecklist)
class StudentDegreeChecklistAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset):
        # data import logic for the StudentDegreeChecklist model here
        # This function will be called when the "Import Data" action is selected in the admin interface

    import_data.short_description = "Import Data"


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset):
        # data import logic for the CourseEnrollment model here
        # This function will be called when the "Import Data" action is selected in the admin interface

    import_data.short_description = "Import Data"
