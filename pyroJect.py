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
		#=====[ root and subdirs	]=====
		self.root_dir = self.make_module_dir(self.path, self.name)
		self.src_dir = self.make_module_dir(self.root_dir, self.name)
		self.test_dir = self.make_module_dir(self.root_dir, 'test')
		if self.data:
			self.data_dir = self.ensure_dir_exists(self.root, 'data')

		#=====[ .gitignore	]=====
		self.make_gitignore()

		#=====[ configure.sh	]=====
		self.make_configure_script()





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
	####################[ SPECIAL FILES ]###########################################
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




