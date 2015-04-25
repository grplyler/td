from setuptools import setup, find_packages
import os

setup(name='td',
      version='0.2.1',
      description='A practical, project based todo manager for all your needs.',
      author='Ryan Plyler',
      author_email='g.r.plyler@gmail.com',
      url='http://github.com/grplyler/td',
      packages=find_packages(),
      data_files=[(os.path.expanduser('~/.td/'), ['data/conf.yml'])],
      install_requires=[
          'peewee',
          'docopt',
          'PyYAML'
      ],
      scripts=['bin/td'],
)
