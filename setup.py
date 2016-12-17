from setuptools import setup, find_packages
import os
import shutil

dirname = os.path.dirname(os.path.abspath(__file__))

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='Watchtower Agent',
      version='0.1',
      description='Install Watchtower Agent',
      long_description=readme(),
      url='http://localhost/watchtower/',
      author='Scott Ehas',
      author_email='ScottEhas@gmail.com',
      license='Proprietary',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      entry_points = {
	     'console_scripts': ['watchtower=watchtower.agent:main'],
      },
      zip_safe=False)


if os.path.isfile(dirname+'/setup.py'):
    print 'done installation'
    print 'removing dir %s' % (dirname)
    shutil.rmtree(dirname)
