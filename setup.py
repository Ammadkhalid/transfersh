from setuptools import find_packages, setup

setup(
name = 'transfersh',
version = '0.1',
packages = find_packages(),
package_dir = {
'transfersh': 'transfersh'
},
author = 'Ammad Khalid',
install_requires = ['requests']
)
