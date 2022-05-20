from django.test import TestCase, Client
from board.models import *
import json


class DetailpageTest(TestCase):

    def test_제목클릭하면_그_질문의_상세정보가_보이기(self):
        # Given
        q1 = Question.objects.create(subject='test1', content='test1')
        client = Client()
        response = self.client.get('board/1', {'json':'json'})
        print(self.client.request())


        # self.assertEqual(response.question.subject, 'test1')


