#!/usr/bin/env python
from setuptools import setup

setup(
	name='slackrealtime',
	version='0.1',
	description='Twisted/Autobahn-based client for the Slack Real-Time Messaging API',
	author='Michael Farrell',
	author_email='micolous+py@gmail.com',
	url='https://github.com/micolous/python-slackrealtime',
	packages=['slackrealtime'],
	package_dir={'slackrealtime': 'src/slackrealtime'},
	install_requires=[
		'autobahn',
		'pytz',
		'requests',
		'Twisted',
		'zope.interface',
		'PyOpenSSL',
		'service_identity',
	],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Framework :: Twisted',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
		'Topic :: Communications :: Chat',
	],
)
