"""Testing Looking Glass Tool"""

import sys
import os.path
import datetime
import unittest

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)

from lookingglass import Timesheet

class TimesheetTestCase(unittest.TestCase):
	
	def setUp(self):
		self.timesheet = Timesheet(os.path.join(root, 'tests/example.yaml'))
		
	def test_meta(self):
		self.assertEqual(self.timesheet.get_project_name(), 'Example Project')
		
	def test_entries(self):
		self.assertEqual(self.timesheet.get_total_entries(), 3)
	
	def test_hours(self):
		self.assertEqual(self.timesheet.get_total_hours(), 6.5)
		
	def test_hours_within(self):
		f = datetime.datetime(2012, 7, 1)
		t = datetime.datetime(2012, 8, 1)
		
		self.assertEqual(self.timesheet.get_hours_within(f, t), 6.5)
		
		f = datetime.datetime(2012, 7, 1)
		t = datetime.datetime(2012, 7, 31)
		
		self.assertEqual(self.timesheet.get_hours_within(f, t), 3.0)
		
if __name__ == '__main__':
	unittest.main()