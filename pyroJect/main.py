"""
Module: main.py
===============

Description:
------------
	
	Contains main PyroJect class. This sets up a directory 
	structure that looks like:

	project_name/
		
		.gitignore
		
		setup.py

		tests/
			__init__.py 
			test_example.py 

		ModuleName/
			__init__.py
			inference.py 	#optional (-d)
			util.py

		data/ 				#optional (-d)
			models/ 		#optional (-d)



Args:
-----

	-d (--data): make it a data-scientific application, including 
					inference base classes and a data directory



Example Usage:
--------------
		
		pyroJect [project_name] [path_to_make] [-d, --data]

	i.e.

		pyroJect strong_ai . -d



##################
Jay Hack
Fall 2014
jhack@stanford.edu
##################
"""
import os
import shutil
import json
import time
import click


class PyroJect(object):
	"""
		Class for maintaining all aspects of the creation 
		of this python module 
	"""
	#=====[ templates	]=====
	base_path = os.path.join(os.path.split(__file__)[0], '..')
	templates_path = os.path.join(base_path, 'templates')

	#=====[ project details	]=====
	name = None
	path = None
	data = False
	author = None
	email = None
	date = None

	def __init__(self, name, path, author, email, data):
		"""
			Merely initializes this project 

			Args:
			-----
				- path: path to make project (short of the name)
				- name: name of project 
				- data: boolean for wether there should be a data dir 
		"""
		self.name = name 
		self.path = path
		self.author = author 
		self.email = email
		self.data = data

		print 'base_path: %s' % self.base_path
		print 'templates_path: %s' % self.templates_path


	def build(self):
		"""
			Main method - creates the entire project
		"""
		self.root_dir = self.make_module_dir(self.path, self.name)
		self.make_source_dir()
		self.make_scripts_dir()
		self.make_tests_dir()
		self.make_data_dir()
		self.make_gitignore()
		self.make_setup_script()







	################################################################################
	####################[ GENERATING FILE HEADERS ]#################################
	################################################################################

	def make_header_head(self, filetype, name):
		"""
			returns a string containing the header for a python file 
			header string

			filetype: Script, Class, etc.
			name: name of the file
		"""
		headline = filetype.capitalize() + ': ' + name
		return headline + '\n'  + '='*len(headline)


	def make_header_body(self, filetype, header_sections):
		"""
			returns a string containing the body of a python file 
			header string 
			when filetype is 'script', includes an 'Arguments' section; 
			otherwise, defaults to just 'Description' and 
		"""
		def make_section(section_name):
			return section_name + ':\n' + '-'*(len(section_name) + 1)

		return '\n\n'.join([make_section(s) for s in header_sections])


	def make_header_foot(self):
		"""
			returns a string containing the footer for a python file 
			header string 
		"""
		return '''##################
{author}
{email}
{date}
##################'''.format(	
								author=self.author, 
								email=self.email, 
								date=self.date
							)


	def make_header(self, filetype, name, header_sections):
		"""
			returns a full header string for a python file 
		"""
		return '''"""
{head}

{body}

{foot}
"""'''.format(	
				head=self.make_header_head(filetype, name), 
				body=self.make_header_body(filetype, header_sections), 
				foot=self.make_header_foot()
			)










	################################################################################
	####################[ GENERATING FILES FROM TEMPLATES ]#########################
	################################################################################

	def get_file_template(self, template_name):
		"""
			returns the file template given by template_name
			as a string 
		"""
		#=====[ Step 1: get the unformatted string	]=====
		unformatted = open(os.path.join(self.templates_path, template_name)).read()

		#=====[ Step 2: format + return	]=====
		return unformatted.format(pyroject_header_foot=self.make_header_foot())


	def make_source_file(self, module_dir, name, contents):
		"""
			Will create a file containing 'contents' in the named module_dir 
			returns path to file
		"""
		#=====[ Step 1: figure out name/path	]=====
		if name[:-3] == '.py':
			path = os.path.join(module_dir, name)
			name = name[:-3]
		else:
			path = os.path.join(module_dir, name + '.py')

		#=====[ Step 2: open file and write	]=====
		open(path, 'w').write(contents)
		return path


	def insert_template(self, module_dir, name):
		"""
			Given a module directory and the name of a template,
			this will format and insert it 
		"""
		contents = self.get_file_template(name)
		self.make_source_file(module_dir, name, contents)









	################################################################################
	####################[ FILESYSTEM UTILITIES ]####################################
	################################################################################

	def ensure_dir_exists(self, path, name):
		"""
			makes the directory if it doesnt already exist;
			returns path to it
		"""
		root = os.path.abspath(os.path.join(path, name))
		if not os.path.exists(root):
			os.mkdir(root)
		return root


	def make_module_dir(self, path, name):
		"""
			makes a directory in the path with an __init__.py
			file in it; returns path to its root
		"""
		module_root = self.ensure_dir_exists(path, name)
		open(os.path.join(module_root, '__init__.py'), 'a').close()
		return module_root






























	################################################################################
	####################[ MAKING SUBDIRS/FILES  ]###################################
	################################################################################

	def make_source_dir(self):
		"""
			makes directory to contain source, complete with main.py with 
			header included;
			sets self.source_dir
		"""
		self.source_dir = self.make_module_dir(self.root_dir, self.name)
		templates = ['example_class.py', 'util.py']
		if self.data:
			templates.append('inference.py')
		map(lambda t: self.insert_template(self.source_dir, t), templates)


	def make_scripts_dir(self):
		"""
			makes directory to contain source, complete with example_script.py 
			with header included;
			sets self.scripts_dir 
		"""
		self.scripts_dir = self.make_module_dir(self.root_dir, 'scripts')
		self.insert_template(self.scripts_dir, 'example_script.py')


	def make_tests_dir(self):
		"""
			makes directory to contain tests, complete with test_EXAMPLE.py 
			with header included;
			sets self.tests_dir 
		"""
		#=====[ Step 1: make tests dir ]=====
		self.tests_dir = self.make_module_dir(self.root_dir, 'tests')
		self.insert_template(self.tests_dir, 'example_test.py')


	def make_data_dir(self):
		"""
			makes a data dir with a subdirectory, 'models',
			if data flag is set 
		"""
		if self.data:
			self.data_dir = self.make_module_dir(self.root_dir, 'data')
			os.mkdir(os.path.join(self.data_dir, 'models'))


	def make_gitignore(self):
		"""
			makes gitignore file in the base directory 
		"""
		gitignore_src = os.path.join(self.templates_path, 'gitignore')
		gitignore_dst = os.path.join(self.root_dir, '.gitignore')
		shutil.copy(gitignore_src, gitignore_dst)


	def make_setup(self):
		"""
			makes a setup.py script that allows you to run 
				python setup.py install 
			in order to install your module
		"""
		unformatted = self.get_file_template('setup')
		setup_contents = unformatted.format(name=self.name, author=self.author, email=self.email)
		setup_dst = os.path.join(self.root_dir, 'setup.py')
		open(setup_dst, 'w').write(setup_contents)







