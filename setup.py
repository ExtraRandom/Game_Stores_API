from distutils.core import setup
import os, re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('Games_Stores_API/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(name='game_stores_api',
      author='Extra_Random',
      author_email='a',
      version=version,
      license='MIT',
      description='a',
      install_requires=requirements,
      packages=['ITAD', 'Origin', 'Playstation', 'Steam', 'Xbox'])



