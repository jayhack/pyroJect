# pyroJect
This project allows one to quickly set up python project skeletons.

by Jay Hack (jhack@stanford.edu), Fall 2014

## Overview
pyroJect takes minimal user input and will set up projects as follows:
```
	project_name/
		.configure.sh
		.gitignore
		project_name/		(source directory)
			__init__.py
			example_class.py
		scripts/
			__init__.py
			example_script.py
		tests/
			__init__.py
			test_EXAMPLE.py
		data/ 				(optional)
```
### example class/script/tests
Each example class/script/test contains preformatted headers. In addition:
* example_script.py contains a preformatted click script, along with imports
* example_test.py contains a preformatted unittest.TestCase class, along with imports.

### configure.sh
configure.sh will set environmental variables as follows:
```
export PROJECT_DIR=`pwd`
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR
export DATA_DIR=`pwd`/data #only if -d is specified
```
this allows you to run
```
In [1]: from my_project import *
```
from within a python script or the interactive console from anywhere 
on your filesystem.

### .gitignore
the .gitignore file will ignore all of the following filetypes:
* .pyc
* .pkl
* .json
* .npy





## Installation
In order to install pyroJect, clone the repository and run configure.sh:
```
	chmod +x configure.sh
	./configure.sh
```
This will add the repository to your $PATH environmental variable as well 
as creates an executable, pyroJect, that will be executed by your default
python.




## Usage:
To create a project named project_name in your current directory:
```
	pyroJect project_name .
```
To optionally include a data directory:
```
	pyroJect project_name . -d
```
or 
```
	pyroJect project_name . --data
```
Creating a project with a data directory will also ensure that the 
$DATA_DIR environmental variable is set.


