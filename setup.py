from distutils.core import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='GameStoresAPI',
      author='Extra_Random',
      author_email='crazyblob11@gmail.com',
      version='0.0.8.3 - test',
      license='MIT',
      description='For helping with the collection of pricing and other data from online game stores.',
      install_requires=requirements,
      packages=['shared',
                'steam',
                # 'GameStoresAPI.Origin',
                # 'GameStoresAPI.Xbox',
                # 'GameStoresAPI.GMG',
                'itad',
                'playstation'])



