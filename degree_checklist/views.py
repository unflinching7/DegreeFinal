from django.shortcuts import render
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment


def all_records(request):
    students = Student.objects.all()
    degree_programs = DegreeProgram.objects.all()
    courses = Course.objects.all()
    degree_checklist_templates = DegreeChecklistTemplate.objects.all()
    student_degree_checklists = StudentDegreeChecklist.objects.all()
    course_enrollments = CourseEnrollment.objects.all()

    return render(request, 'degree_checklist/all_records.html', {
        'students': students,
        'degree_programs': degree_programs,
        'courses': courses,
        'degree_checklist_templates': degree_checklist_templates,
        'student_degree_checklists': student_degree_checklists,
        'course_enrollments': course_enrollments,
    })
