from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hotel_app/__init__.py
from hotel_app import __version__ as version

setup(
	name="hotel_app",
	version=version,
	description="As a practical example for participants in the Frappe development training course",
	author="MohamedAbdulsalam",
	author_email="moha2016it@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
