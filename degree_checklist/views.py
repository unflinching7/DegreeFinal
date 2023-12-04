from django.shortcuts import render
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment
from reportlab.pdfgen import canvas
import csv
from django.http import HttpResponse


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

def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sample.csv"'

    csv_writer = csv.writer(response)

    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['John Doe', 25, 'New York'])
    csv_writer.writerow(['Jane Smith', 30, 'San Francisco'])
    # Add more rows as needed

    return response

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sample.pdf"'

    # Create a PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 800, "Hello world.")

    # Close the PDF object cleanly, and done.
    p.showPage()
    p.save()

    return response


