from setuptools import setup, find_packages
# run the file with "pip install -e." this create a folder "src.egg-info"

'''setup.py is a python file, the presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

This allows you to easily install Python packages. Often it's enough to write:

$ pip install . 
pip will use setup.py to install your module. Avoid calling setup.py directly.
https://stackoverflow.com/questions/1471994/what-is-setup-py
'''

setup(
    name="src",
    version="0.0.1", # just version
    description="its a wine Q package",
    author="Naveen Vinayak S",
    packages=find_packages(),
    license="MIT"
)