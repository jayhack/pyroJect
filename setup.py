from setuptools import setup, find_packages

setup(
		name='pyroJect',
		version='0.0.2',
		author='Jay Hack',
		author_email='jhack@stanford.edu',
		description='utility to quickly create python project skeletons',
		packages=find_packages(),
		include_package_data=True,
		package_data={
			'templates':['datascience']
		},
		scripts=['bin/make_pyroJect.py'],
		install_requires=[
			'click',
		]
)