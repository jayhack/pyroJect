from setuptools import setup, find_packages

setup(
		name='{name}',
		version='0.0.1',
		author='{author}',
		author_email='{email}',
		description='',
		packages=find_packages(),
		include_package_data=True,
		install_requires=[
			'click'
		]
)