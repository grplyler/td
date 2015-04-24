from setuptools import setup, find_packages

setup(name='td',
      version='0.2.0',
      description='A practical, project based todo manager for all your needs.',
      author='Ryan Plyler',
      author_email='g.r.plyler@gmail.com',
      url='http://github.com/grplyler/td',
      packages=find_packages(),
      include_package_data=True,
      package_data={'td': ['data/*']},

      install_requires=[
          'peewee',
          'docopt',
          'PyYAML'
      ],
      scripts=['bin/td'],
)
