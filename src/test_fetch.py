from unittest import TestCase
from src.fetcher.fetch import read_spreadsheet
import csv
import os

class TestReadSpreadsheet(TestCase):
	def test_read_spreadsheet(self):
		sample_sheet = [
			["not a link", "also not a link", "https://www.google.com"],
			["https://www.youtube.com/watch?v=h828fACU9ik", "TnE 100 Days of Talking Episode 1", "description"],
			["Misshapen data", "https://www.youtube.com/watch?v=SG2UpSHZgi0"],
			["Nothing to see here..."]
		]

		test_filename = 'sample_sheet.csv'

		with open(test_filename, 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerows(sample_sheet)


		test_output_dir, test_video_files = read_spreadsheet(test_filename)

		self.assertEqual(test_output_dir, os.path.join(os.getcwd, 'sample_sheet'))

		self.assertIsNotNone(test_video_files)

		self.assertIsInstance(test_video_files, list)

		self.assertTrue(len(test_video_files) == 2)
		
		for item in ['https://www.youtube.com/watch?v=h828fACU9ik', 'https://www.youtube.com/watch?v=SG2UpSHZgi0']:
			self.assertIn(item, test_video_files)

		self.assertNotIn('https://www.google.com', test_video_files)

		os.remove('sample_sheet.csv')

