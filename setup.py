import re
from setuptools import setup


version = re.search("__version__ = '([^']+)'",
                    open('torrent_checker.py').read()).group(1)

setup(name='torrent checker',
      author='Bryce Boe',
      author_email='bbzbryce@gmail.com',
      description='A program to check for the existance of files for seeding.',
      install_requires=['pyrobase', 'pyrocore'],
      keywords=['bittorrent'],
      py_modules = ['torrent_checker'],
      version=version,
      entry_points = {'console_scripts':
                          ['torrent_checker = torrent_checker:main']}

)
