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


def ensure_dir_exists(path, name):
	"""
		makes the directory if it doesnt already exist;
		returns path to it
	"""
	root = os.path.join(path, name)
	if not os.path.exists(root):
		os.mkdir(root)
	return root


def make_module_dir(path, name):
	"""
		makes a directory in the path with an __init__.py
		file in it; returns path to its root
	"""
	module_root = ensure_dir_exists(path, name)
	open(os.path.join(module_root, '__init__.py'), 'a').close()
	return module_root



@click.command()
@click.argument('project_name', type=str)
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--data', '-d', is_flag=True)
def pyroJect(project_name, project_path, data):

	#=====[ Step 1: root dir	]=====
	root_dir = make_module_dir(project_path, project_name)

	#=====[ Step 2: top-level subdirs	]=====
	src_dir = make_module_dir(root_dir, project_name)
	tests_dir = make_module_dir(root_dir, 'tests')
	if data:
		data_dir = ensure_dir_exists(root_dir, 'data')


if __name__ == '__main__':
	pyroJect()




