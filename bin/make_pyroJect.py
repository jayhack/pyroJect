"""
Script: make_pyroject.py
========================

Description:
------------
	
	Sets up a project directory structure that looks like:

	project_name/
		
		README.md

		.gitignore
		
		setup.py

		project_name/
			__init__.py
			util.py
			example_class.py
			inference/
				base_inference.py
				scipy_inference.py

		scripts/

		tests/
			__init__.py 
			example_test.py 

		data/ 				
			models/ 



Args:
-----

	-n (--name): name of the project 
	-p (--path): path to make the project 
	-a (--author): author of the project
	-e (--email): email associated with the project
	-t (--template_name): name of the template to use

	All arguments will be prompted for if not provided, except for -d.



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
@click.option('-t','--template_name', prompt=True)
def make_project(project_name, path, author, email, template_name):
	PyroJect(project_name, author, email, template_name).build(path)


if __name__ == '__main__':
	make_project()