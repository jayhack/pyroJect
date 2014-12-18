"""
Script: pyroJect.py
===================

Description:
------------
	
	Sets up a project directory structure that looks like:

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
import click
from pyroJect import *

@click.command()
@click.argument('project_name', type=str)
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--data', '-d', is_flag=True)
def make_project(project_name, project_path, data):
	PyroJect(project_name, project_path, data).build()


if __name__ == '__main__':
	make_project()