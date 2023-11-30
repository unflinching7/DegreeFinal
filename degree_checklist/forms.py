from django import forms
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_enrollment_year(self):
        enrollment_year = self.cleaned_data.get('EnrollmentYear')

        # validation logic
        if enrollment_year < 2000:
            raise forms.ValidationError("Enrollment year must be after 2000.")

        return enrollment_year

class DegreeProgramForm(forms.ModelForm):
    class Meta:
        model = DegreeProgram
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class DegreeChecklistTemplateForm(forms.ModelForm):
    class Meta:
        model = DegreeChecklistTemplate
        fields = '__all__'

class StudentDegreeChecklistForm(forms.ModelForm):
    class Meta:
        model = StudentDegreeChecklist
        fields = '__all__'

class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

class DataImportForm(forms.Form):
    data_file = forms.FileField(label="Select a data file for import")
