from django.test import TestCase
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment


class StudentModelTest(TestCase):
    def test_str_representation(self):
        student = Student(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        self.assertEqual(str(student), "John Doe")


class DegreeProgramModelTest(TestCase):
    def test_str_representation(self):
        degree_program = DegreeProgram(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        self.assertEqual(str(degree_program), "Computer Science")


class CourseModelTest(TestCase):
    def test_str_representation(self):
        course = Course(CourseName="Introduction to Programming", CourseCode="CS101", CreditHours=3)
        self.assertEqual(str(course), "Introduction to Programming")


class DegreeChecklistTemplateModelTest(TestCase):
    def test_str_representation(self):
        degree_program = DegreeProgram(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        checklist_template = DegreeChecklistTemplate(TemplateName="CS Degree Checklist", AcademicYear="2022", DegreeProgram=degree_program)
        self.assertEqual(str(checklist_template), "CS Degree Checklist")


class StudentDegreeChecklistModelTest(TestCase):
    def test_str_representation(self):
        student = Student(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        degree_program = DegreeProgram(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        checklist_template = DegreeChecklistTemplate(TemplateName="CS Degree Checklist", AcademicYear="2022", DegreeProgram=degree_program)
        student_degree_checklist = StudentDegreeChecklist(ChecklistName="John's Checklist", Status="active", Student=student, Template=checklist_template)
        self.assertEqual(str(student_degree_checklist), "John's Checklist")


class CourseEnrollmentModelTest(TestCase):
    def test_str_representation(self):
        student = Student(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        course = Course(CourseName="Introduction to Programming", CourseCode="CS101", CreditHours=3)
        enrollment = CourseEnrollment(EnrollmentStatus="enrolled", Student=student, Course=course)
        self.assertEqual(str(enrollment), "John Doe - Introduction to Programming")

