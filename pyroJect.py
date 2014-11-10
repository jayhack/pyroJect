'''
Script: pyroJect.py
===================

Description:
------------
	
	Uses and click modules to quickly set up a python project 
	in the following format:

	project_name/
		.configure.sh
		.gitignore
		tests/
		ModuleName/
			__init__.py
		data/ 				#optional
		setup.py


Args:
-----

	-d: include a data directory


Example Usage:
--------------
		
		pyroJect [project_name] [path_to_make] [-d, --data]

	i.e.

		pyroject strong_ai . -d



##################
Jay Hack
Fall 2014
jhack@stanford.edu
##################
'''
import os
import click

class PyroJect(object):
	"""
		Class for maintaining all aspects of the creation 
		of this python module 
	"""
	author = "Jay Hack"
	email = "jhack@stanford.edu"
	date = "Fall 2014"

	def __init__(self, name, path, data):
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
		self.data = data


	def build(self):
		"""
			actually creates the full project 
		"""
		#=====[ Step 1: root dir and special files	]=====
		self.root_dir = self.make_module_dir(self.path, self.name)
		self.make_gitignore()
		self.make_configure_script()

		#=====[ Step 2: subdirectories	]=====
		self.make_source_dir()
		self.make_scripts_dir()
		self.make_tests_dir()
		if self.data:
			self.data_dir = self.ensure_dir_exists(self.root, 'data')





	################################################################################
	####################[ FILESYSTEM UTILS ]########################################
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
	####################[ FILE FORMATTING ]#########################################
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
%s
%s
%s
##################''' % (self.author, self.email, self.date)


	def make_header(self, filetype, name, header_sections):
		"""
			returns a full header string for a python file 
		"""
		return '''"""
%s

%s

%s
"""''' 	% (	
			self.make_header_head(filetype, name), 
			self.make_header_body(filetype, header_sections), 
			self.make_header_foot()
		)



	def make_example_source_file(self, module_dir, name, contents):
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





	################################################################################
	####################[ SOURCE  ]#################################################
	################################################################################

	def make_source_template(self, name):
		"""
			makes a source file with formatting already there 
		"""
		header = self.make_header('Class', name, ['Description', 'Usage'])
		self.make_example_source_file(self.source_dir, name, header)


	def make_source_dir(self):
		"""
			makes directory to contain source, complete with main.py with 
			header included;
			sets self.source_dir
		"""
		#=====[ Step 1: make source dir	]=====
		self.source_dir = self.make_module_dir(self.root_dir, self.name)

		#=====[ Step 2: make example_class.py ]=====
		main = self.make_source_template('example_class')







	################################################################################
	####################[ SCRIPTS ]#################################################
	################################################################################

	def make_script_body(self, script_name):
		"""
			returns a string containing a click command and the 
			additional utilities needed to execute it 
		"""
		if script_name.endswith('.py'):
			script_name = script_name[:-3]

		return """
import click
@click.command()
def %s():
	pass 

if __name__ == '__main__':
	%s()
""" % (script_name, script_name)


	def make_script_template(self, name):
		"""
			makes a script template, including headers 
			and click
		"""
		header = self.make_header('Script', name, ['Description', 'Arguments', 'Usage'])
		click_main = self.make_script_body(name)
		self.make_example_source_file(self.scripts_dir, name, header + click_main)


	def make_scripts_dir(self):
		"""
			makes directory to contain source, complete with example_script.py 
			with header included;
			sets self.scripts_dir 
		"""
		#=====[ Step 1: make source dir	]=====
		self.scripts_dir = self.make_module_dir(self.root_dir, 'scripts')

		#=====[ Step 2:	make example_script.py]=====
		self.make_script_template('example_script')









	################################################################################
	####################[ TESTS ]###################################################
	################################################################################

	def make_tests_body(self, test_name):
		"""
			returns a string containing the basics for a test 
		"""
		return """
import unittest
import nose
from nose.utils import *

class Test_EXAMPLE(unittest.TestCase):

	################################################################################
	####################[ setUp/tearDown	]#######################################
	################################################################################

	def setUp():
		pass

	def tearDown():
		pass


	################################################################################
	####################[ EXAMPLE TESTS	]###########################################
	################################################################################

	def test_EXAMPLE():
		pass
"""

	def make_test_template(self, name):
		"""
			makes a test template. including headers, nosetest import and 
			basic class 
		"""
		header = self.make_header('Test', name, ['Description'])
		body = self.make_tests_body(name)
		self.make_example_source_file(self.tests_dir, name, header + body)


	def make_tests_dir(self):
		"""
			makes directory to contain tests, complete with test_EXAMPLE.py 
			with header included;
			sets self.tests_dir 
		"""
		#=====[ Step 1: make tests dir ]=====
		self.tests_dir = self.make_module_dir(self.root_dir, 'tests')

		#=====[ Step 2: make test_EXAMPLE.py	]=====
		self.make_test_template('test_EXAMPLE')









	################################################################################
	####################[ GITIGNORE ]###############################################
	################################################################################

	def make_gitignore(self):
		"""
			makes gitignore file in the base directory 
		"""
		gitignore_str = """#=====[ Temporary Files	]=====
*.pkl
*.json
*.npy
*.pyc
"""
		gitignore = open(os.path.join(self.root_dir, '.gitignore'), 'w')
		gitignore.write(gitignore_str)






	################################################################################
	####################[ CONFIGURE ]###############################################
	################################################################################

	def make_configure_script(self):
		"""
			makes a .configure.sh script that will include the 
			current module in your pythonpath
		"""
		configure_str = """export PROJECT_DIR=%s
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR
""" % self.root_dir

		if self.data:
			configure_str += """\nexport DATA_DIR=%s""" % self.data_dir
	
		configure = open(os.path.join(self.root_dir, 'configure.sh'), 'w')
		configure.write(configure_str)




@click.command()
@click.argument('project_name', type=str)
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--data', '-d', is_flag=True)
def pyroJect(project_name, project_path, data):

	PyroJect(project_name, project_path, data).build()


if __name__ == '__main__':
	pyroJect()




