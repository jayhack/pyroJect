"""
Script: make_pyroject.py
========================

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
@click.option('-n', '--project_name', type=str, prompt=True)
@click.option('-p', '--path', type=click.Path(exists=True), prompt=True)
@click.option('-a', '--author', type=str, prompt=True)
@click.option('-e', '--email', type=str, prompt=True)
@click.option('-d','--data', is_flag=True)
def make_project(project_name, path, author, email, data):
	PyroJect(project_name, path, author, email, data).build()


if __name__ == '__main__':
	make_project()