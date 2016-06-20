import unittest
from notesapplication import NotesApplication

class NotesApplicationTest(unittest.TestCase):
	'''Testing the NotesApplication
	'''
	def test_author_name_instantiated_with_clas_is_same_as_par(self):
		obj = NotesApplication('Lolo')
		self.assertEqual(obj.author,'Lolo')

	def test_instance_of_created_is_of_type_class(self):

		obj = NotesApplication('Lolo')
		self.assertIsInstance(obj, NotesApplication, msg='should be an instance of `NotesApplication`')

	def test_result_get_note_using_note_id_is_of_type_string(self):
		obj = NotesApplication('Lolo')
		obj.create('This is Andela')
		note = obj.get_note(0)

		self.assertEqual(True, type(note) is str)
		
	


if __name__=='__main__':
	unittest.main()