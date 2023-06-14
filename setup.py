from setuptools import setup, find_packages

setup(
    name="advent_of_code_2022",
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
)
