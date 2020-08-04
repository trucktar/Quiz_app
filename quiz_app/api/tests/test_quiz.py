from django.test import TestCase
from quiz_app.api.models import User, Quiz, Question, Answer, Attempt

class TestQuiz(TestCase):
    def setUp(self):
        user_profile = User.objects.create(id=1, username='jorim', email='jorim.webdev@gmail.com', first_name='Jorim', last_name='Midumbi', password='moringa81').profile

        self.quiz1 = Quiz.objects.create(id=1, title='Django Quiz', description=' Django interview questions',duration='00:30', profile=user_profile)
        self.quiz2 = Quiz.objects.create(id=2, title='Flask Quiz', description=' Flask interview questions',duration='00:30', profile=user_profile)
        self.quiz3 = Quiz.objects.create(id=3, title='Angular Quiz', description=' Angular interview questions',duration='00:30', profile=user_profile)

        self.question1 = Question.objects.create(id=1, content='Django test question', quiz=self.quiz1)

    def test_save_quiz(self):
        self.assertTrue(self.quiz1.title == 'Django Quiz')
        self.assertTrue(self.quiz2.title == 'Flask Quiz')
        self.assertTrue(self.quiz3.title == 'Angular Quiz')

    def test_save_questions(self):
        self.question2 = Question.objects.create(id=2, content='Flask test question', quiz=self.quiz2)
        self.question3 = Question.objects.create(id=3, content='Angular test question', quiz=self.quiz3)

        self.assertIn(self.question2, self.quiz2.questions)
        self.assertIn(self.question3, self.quiz3.questions)

    def test_save_answers(self):
        question4 = Question.objects.create(id=4, content='Flask test question', quiz=self.quiz2)

        self.answer1 = Answer.objects.create(id=1, value='Flask test answer 1', is_correct=True, question=question4)
        self.answer2 = Answer.objects.create(id=2, value='Flask test answer 2', is_correct=False, question=question4)

        self.assertIn(self.answer1, question4.answers)
        self.assertIn(self.answer2, question4.answers)
        self.assertTrue(question4.check_if_correct(self.answer1.value))
        self.assertFalse(question4.check_if_correct(self.answer2.value))
