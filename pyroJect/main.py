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

	def __init__(self, name, author, email, template_name):
		"""
			fills in metadata about the project

			Args:
			-----
				- name: project name
				- author: project author(s)
				- email: email(s) associated with project
				- template_name: name of the template to use
		"""
		self.template_name = template_name
		self.metadata = {
							'name':name,
							'author':author,
							'email':email,
							'date':time.strftime('%B %Y'),
						}

		self.filename_trans_table = {
							'GITIGNORE':'.gitignore',
							'SRC':self.metadata['name'],
							self.template_name:self.metadata['name']
						}


	def get_template_dir(self, template_name):
		"""
			template name -> path of template directory 
		"""
		pyroject_dir = os.path.join(os.path.split(__file__)[0], '..')
		templates_dir = os.path.join(pyroject_dir, 'templates')
		print templates_dir
		print os.listdir(templates_dir)
		if not template_name in os.listdir(templates_dir):
			raise Exception("Template named %s does not exist" % template_name)
		else:
			return os.path.join(templates_dir, template_name)


	def copy_project_template(self, template_name, project_path):
		"""
			moves the project template to desired location 
		"""
		shutil.copytree(self.get_template_dir(template_name), project_path)


	def modify_template_filenames(self, project_path):
		"""
			changes file/directory names according to self.filename_trans_table
		"""
		for root, dirs, files in os.walk(project_path):
			for k, v in self.filename_trans_table.items():
				if k in dirs + files:
					shutil.move(os.path.join(root, k), os.path.join(root, v))


	def modify_template_filecontents(self, project_path):
		"""
			changes contents of file according to self.metadata
		"""
		for root, dirs, files in os.walk(project_path):
			for f in files:
				filepath = os.path.join(root, f)
				formatted = open(filepath, 'r').read().format(**self.metadata)
				open(filepath,'w').write(formatted)


	def build(self, path):
		"""
			creates the entire project 

			Args:
			-----
			- path: location to create project
		"""
		project_dir = os.path.join(path, self.metadata['name'])
		self.copy_project_template(self.template_name, project_dir)
		self.modify_template_filenames(project_dir)
		self.modify_template_filecontents(project_dir)
