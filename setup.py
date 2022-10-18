from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shop/__init__.py
from shop import __version__ as version

setup(
	name="shop",
	version=version,
	description="shop management",
	author="sakiya",
	author_email="123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
