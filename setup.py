from setuptools import *

setup(name='ignoramus',
	version='0.1',
	description='A command line tool for generating .gitignore files.',
	url='https://github.com/cornjuliox/ignoramus',
	author='Enrico Jr Tuvera',
	author_email='enricojr.tuvera@gmail.com',
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		'click==6.7'
	],
	zip_safe=False,
	entry_points='''
		[console_scripts]
		ignoramus=ignoramus.app:supermain
	''')
