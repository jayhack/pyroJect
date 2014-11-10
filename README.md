# pyroJect
This project allows one to quickly set up python project skeletons.

by Jay Hack (jhack@stanford.edu), Fall 2014

## Overview
pyroJect takes minimal user input and will set up projects as follows:
```
	project_name/
		.configure.sh
		.gitignore
		project_name/			(source directory)
			__init__.py
			example_class.py
		scripts/				
			__init__.py
			example_script.py
		tests/					(nosetests)
			__init__.py
			test_EXAMPLE.py
		data/ 					(optional; specify with -d)
```
#### example class/script/tests
Each example class/script/test contains preformatted headers. In addition:

- scripts/example_script.py contains a preformatted click script, along with imports

- tests/example_test.py contains a preformatted unittest.TestCase class, along with imports.


#### configure.sh
configure.sh will set environmental variables as follows:
```
export PROJECT_DIR=`pwd`
export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR
export DATA_DIR=`pwd`/data #only if -d is specified
```
This allows you to import the module from anywhere on your system:
```
In [1]: import my_project
```

#### .gitignore
.gitignore will instruct git to ignore files as follows:
```
*.pyc
*.pkl
*.json
*.npy
```
These are typically temporary files; this may not be appropriate for all python programs,
however.




## Installation
In order to install pyroJect, clone the repository and run configure.sh:
```
	chmod +x configure.sh
	./configure.sh
```
This will:

- add pyroJect to your $PATH
- add well-marked in your ~/.bash_profile to always include pyroJect in your $PATH
- create an executable, ./pyroJect, that will be run by your default python




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
$DATA_DIR environmental variable is set when you run your project's 
configure.sh


