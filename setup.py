import versioneer
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import numpy as np

setup(name='parcels',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      long_description="Lagrangian particle tracking framework",
      long_description="""Framework for Lagrangian tracking of virtual
      ocean particles in the petascale age.""",
      url='http://www.oceanparcels.org',
      author="Imperial College London",
      license='MIT',
      packages=find_packages(exclude=['docs', 'examples', 'indlude', 'scripts', 'tests']),
      install_requires=['numpy', 'sympy', 'cgen', 'cachetools', 'enum34'],
      test_requires=['pytest', 'flake8', 'pytest-ipynb'])
)
