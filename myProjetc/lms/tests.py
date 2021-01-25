from django.test import TestCase
from .models import Assignment, Assignment_answer
import datetime
from django.utils import timezone

# Create your tests here.


class ModelTestCase(TestCase):
    def setUp(self):
        now = datetime.datetime.now()
        self.assignment_user_id = 12
        self.assignment_course_id = "1365"
        self.assignment_file_id = "789"
        self.assignment_description = "a new assignment"
        self.assignment_start_date = timezone.now()
        self.assignment_deadline = timezone.now() + datetime.timedelta(days=30)
        self.assignment = Assignment(user_id = self.assignment_user_id, course_id= self.assignment_course_id, file_id = self.assignment_file_id, description = self.assignment_description, start_date =self.assignment_start_date, deadline = self.assignment_deadline)


    def test_model_can_create_a_Assignment(self):
        old_count = Assignment.objects.count()
        self.assignment.save()
        new_count = Assignment.objects.count()
        self.assertNotEqual(old_count, new_count)


class Model2TestCase(TestCase):
        def setUp(self):
            self.assignment_answer_user_id = 12
            self.assignment_answer__course_id = "1365"
            self.assignment_answer__file_id = "789"
            self.assignment_answer__description = "a new assignment"
            self.assignment__answer_date_of_upload = timezone.now()
            self.assignment_answer = Assignment_answer(user_id = self.assignment_answer_user_id, course_id= self.assignment_answer_course_id, file_id = self.assignment_answer_file_id, description = self.assignment_answer_description, date_of_upload =self.assignment_answer_date_of_upload)

        def test_model_can_create_a_Assignment_answer(self):
            old_count = Assignment_answer.objects.count()
            self.assignment_answer.save()
            new_count = Assignment_answer.objects.count()
            self.assertNotEqual(old_count, new_count)