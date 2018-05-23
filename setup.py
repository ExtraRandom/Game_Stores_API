from distutils.core import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('Games_Stores_API\__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(name='GameStoresAPI',
      author='Extra_Random',
      author_email='crazyblob11@gmail.com',
      version=version,
      license='MIT',
      description='This is where the description would go',
      install_requires=requirements,
      packages=['ITAD',
                # 'Origin',
                'Playstation',
                'Steam',
                # 'Xbox'
                ])



