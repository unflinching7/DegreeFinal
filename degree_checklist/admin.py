from django.contrib import admin
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment

# Register models
admin.site.register(Course)
admin.site.register(DegreeChecklistTemplate)
admin.site.register(StudentDegreeChecklist)
admin.site.register(CourseEnrollment)

# Add import_data function outside the admin classes
def import_data(modeladmin, request, queryset):
    # data import logic for the model here
    # This function will be called when the "Import Data" action is selected in the admin interface
    messages.success(request, "Data imported successfully.")
    return redirect('admin:index')

# Short description for the import_data action
import_data.short_description = "Import Data"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(DegreeProgram)
class DegreeProgramAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(DegreeChecklistTemplate)
class DegreeChecklistTemplateAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(StudentDegreeChecklist)
class StudentDegreeChecklistAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    actions = [import_data]


