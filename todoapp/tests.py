from django.test import TestCase
from .models import Todo

# Create your tests here.

class TodosTest(TestCase):
   def setup(self):
       title=todo(titlename="organize")
       todo=Todo(todotitle='organizing', todotext='organize the bedroom')
       return todo
       
    def test_string(self):
       todo = self.setup()
       self.assertEqual(str(todo), todo.todotitle)

   def test_table(self):
       self.assertEqual(str(Todo._meta.db_table), 'todotitle')
