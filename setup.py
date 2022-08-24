import setuptools

file = open('README', 'r')
detail = file.read()
file.close()

setuptools.setup(
	name = 'eratos',
	version = '0.0.1',
	author = 'gbida',
	description = 'A python module to get the prime number',
	long_description = detail,
	url = 'https://github.com/gbida/eratos',
	license = '',
	packages = setuptools.find_packages(),
	classifiers = [
		'Programming Language :: Python :: 3.7.3',
		'License :: ',
		'Operating System :: OS Independent',
	],
	python_requires = '>=3.7.3',
)