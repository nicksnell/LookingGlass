#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Looking Glass - Web application builder

from setuptools import setup, find_packages
from lookingglass import __version__

long_description = """Looking Glass - Timesheet analyzer"""

setup(
	name='Looking Glass',
	version=__version__,
	description='Looking Glass',
	long_description=long_description,
	author='Nick Snell',
	author_email='nick@orpo.co.uk',
	url='https://github.com/nicksnell/LookingGlass',
	download_url='https://github.com/nicksnell/LookingGlass',
	license='Private',
	platforms=['Linux',],
	classifiers=[
		'Environment :: Web Environment',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
	],
	zip_safe=True,
	packages=find_packages(exclude=['tests',]),
	dependency_links = [
		'pyyaml',
	],
	entry_points = {
		'console_scripts': [
			
		]
	},
	install_requires=[
	],
	extras_require={}
)
