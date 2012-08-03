"""Looking Glass - Timesheet analyzer & builder"""

import os.path
import datetime
import time

import yaml

__version__ = '0.1'

class TimesheetException(Exception): pass

class TimesheetManager(object):
	
	def __init__(self, f):
		"""Read a timesheet file"""
		
		if not os.path.exists(f):
			raise TimesheetException('Timesheet does not exist!')
		
		try:
			conent = open(f).read()
		except IOError:
			raise TimesheetException('Timesheet could not be read!')
			
		# Parse the document
		self.yaml = yaml.load(conent)
		self._filename = f
		
	def save(self):
		# TODO: Save timesheet.
		pass
	
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
	
	def add_hours(self, from_date, to_date, desc=''):
		"""Add hours to the timesheet"""
		
		work = {
			'from': from_date,
			'to': to_date, 
			'desc': desc
		}
		
		self.yaml['work'].append(work)
	
	@staticmethod
	def difference_in_hours(seconds):
		return ((float(seconds) / 60.0) / 60.0)
	