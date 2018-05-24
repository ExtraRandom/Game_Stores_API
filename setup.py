from distutils.core import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='GameStoresAPI',
      author='Extra_Random',
      author_email='crazyblob11@gmail.com',
      version='0.0.3',
      license='MIT',
      description='This is where the description would go',
      install_requires=requirements,
      packages=['GameStoresAPI.Shared',
                'GameStoresAPI.Steam',
                # 'GameStoresAPI.Origin',
                # 'GameStoresAPI.Xbox',
                'GameStoresAPI.ITAD',
                'GameStoresAPI.Playstation'])



