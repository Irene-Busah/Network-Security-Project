"""
setup.py
===========

Setting up the python package
"""


# importing the necessary libraries
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """Returns list of requirements"""

    requirement_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        raise print("FIle not found")
    
    return requirement_list

# print(get_requirements())

setup(
    name="Network-Security",
    version="0.0.1",
    author='Irene Busah',
    author_email="i.busah@alumni.alueducation.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
