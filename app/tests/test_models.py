from django.test import TestCase
from ..models import *
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData :Some Text")
        pass
    def setUp(self):
        print("setUp:Text")
        pass
    
    def test_false_is_false(self):
        print("Method:false if false")
        self.assertFalse(False)
    
    def test_false_is_true(self):
        print("Method:false is true")
        self.assertTrue(True)
    
    def test_one_plus_one_equls_two(self):
        print("Method:equals two")
        post=Posts()
        self.assertEqual(1+1,2)

    # def test_compare_numbers(self):
    #     post=Posts()
    #     self.assertEqual(post.get_number(),9)

    # def test_compare_words(self):
    #     post=Posts()
    #     self.assertEqual(post.get_title(),"Alikhan")

#    python manage.py test --verbosity=2
#    python manage.py test --parllel auto several corses more faster