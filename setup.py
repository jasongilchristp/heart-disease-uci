## used to build an entire ML application as a package

from setuptools import find_packages, setup  
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='heart-disease-uci',
    version='0.0.1',
    author='Jason Gilchrist P',
    author_email="jason.gilchrist.p@gmail.com",
    install_requires = get_requirements('requirements.txt')
)