try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(name='freeboxctrl',
      version='0.1',
      description='Control your Freebox',
      author='Oxeo',
      author_email='oxeo@noreply.fr',
      url='https://github.com/oxeo/freeboxcontrol',
      packages=find_packages(),
      install_requires=['simplejson'],
)
