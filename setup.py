from distutils.core import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='GameStoresAPI',
      author='Extra_Random',
      author_email='crazyblob11@gmail.com',
      version='0.0.7.1',
      license='MIT',
      description='For helping with the collection of pricing and other data from online game stores.',
      install_requires=requirements,
      packages=['GameStoresAPI.Shared',
                'GameStoresAPI.Steam',
                # 'GameStoresAPI.Origin',
                # 'GameStoresAPI.Xbox',
                # 'GameStoresAPI.GMG',
                'GameStoresAPI.ITAD',
                'GameStoresAPI.Playstation'])



