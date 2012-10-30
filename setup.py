import os
import re
from setuptools import setup

MODULE_NAME = 'torrent_checker'

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
VERSION = re.search("__version__ = '([^']+)'",
                    open('{0}.py'.format(MODULE_NAME)).read()).group(1)

setup(name=MODULE_NAME,
      author='Bryce Boe',
      author_email='bbzbryce@gmail.com',
      classifiers=['License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      description='A program to check for the existance of files for seeding.',
      entry_points={'console_scripts': ['{0} = {0}:main'.format(MODULE_NAME)]},
      install_requires=['pyrobase', 'pyrocore'],
      keywords=['bittorrent'],
      license='Simplified BSD License',
      long_description=README,
      py_modules=[MODULE_NAME],
      url='https://github.com/bboe/torrent_checker',
      version=VERSION)
