# pyroJect
Single-command python project setup.

by Jay Hack (jhack@stanford.edu), Fall 2014

## Overview
pyroJect takes minimal user input and will set up projects as follows:
```
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
```
#### example class/script/tests
Each example class/script/test contains preformatted headers. In addition:

- scripts/example_script.py contains a preformatted click script, along with imports

- tests/example_test.py contains a preformatted unittest.TestCase class, along with imports.

### inference and util
If you choose to make it a data-scientific app (using the -d flag), this will add 
the file inference.py to the main source directory, as well as util.py. inference.py
contains abstract classes for performing inferences and util.py contains utilities
for interfacing. 

#### .gitignore
.gitignore will instruct git to ignore files as follows:
```
	#=====[ Setup Files ]=====
	build
	dist
	*.egg-info
	templates

	#=====[ Temporary Files	]=====
	*.pyc
	*.pkl
	*.json
	*.npy
	*~
```
This may not be appropriate for all python programs.



## Installation
In order to install pyroJect, clone the repository and run the following
```
	python setup.py install
```
This will ensure that you can run 
```
	make_pyroject.py [...]
```
in order to make new pyrojects.



## Usage:
Note that all options will be prompted for if not provided, with the 
exception of the -d flag.

To create a project named project_name in your current directory:
```
	make_pyroject.py --name project_name --path .
```
To optionally make it a data-scientific application:
```
	pyroJect --name project_name --path . -d
```


