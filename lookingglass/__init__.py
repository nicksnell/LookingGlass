"""Looking Glass - Timesheet analyzer"""

import os.path
import datetime
import time

import yaml

__version__ = '0.1'

class TimesheetException(Exception): pass

class TimesheetManager(object):
	pass
	
class Timesheet(object):
	
	def __init__(self, f):
		"""Read a timesheet file"""
		
		if not os.path.exists(f):
			raise TimesheetException('Can not read Timesheet!')
		
		# Parse the document
		self.yaml = yaml.load(open(f).read())
	
	def get_project_name(self):
		return self.yaml['project']
		
	def get_total_entries(self):
		return len(self.yaml['work'])
		
	def get_total_hours(self):
		"""Get the total hours logged in the timesheet"""
		
		hours = 0.0
		
		for entry in self.yaml['work']:
			seconds = (entry['to'] - entry['from']).seconds
			hours += self.difference_in_hours(seconds)
			
		return hours
	
	def get_hours_within(self, from_date, to_date):
		"""Get the total hours within two dates"""
		
		hours = 0.0
		
		for entry in self.yaml['work']:
			if entry['from'] > from_date and entry['to'] < to_date:
				seconds = (entry['to'] - entry['from']).seconds
				hours += self.difference_in_hours(seconds)
			
		return hours
	
	@staticmethod
	def difference_in_hours(seconds):
		return ((float(seconds) / 60.0) / 60.0)
	