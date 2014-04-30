#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='flask-peewee',
    version='0.6.6',
    url='https://github.com/rembish/flask-peewee',
    license='BSD',
    author='Charles Leifer',
    author_email='coleifer@gmail.com',
    maintainer='Aleksey Rembish',
    maintainer_email='alex@rembish.org',
    description='Peewee integration for Flask',
    packages=find_packages(),
    package_data={
        'flask_peewee': [
            'static/*/*.css',
            'static/*/*.js',
            'static/*/*.gif',
            'static/*/*.png',
            'templates/*.html',
            'templates/*/*.html',
            'templates/*/*/*.html',
            'tests/*.html',
            'tests/*/*.html',
        ],
    },
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'peewee>2.0.6', 'wtf-peewee'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='runtests.runtests',
)
