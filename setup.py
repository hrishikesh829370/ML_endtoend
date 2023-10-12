from setuptools import find_packages, setup
from typing import List


HYPHEN_E = '_e.'
def get_requirments (file_path:str)->List[str]:
    '''
    this fun will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)



    

setup (
name = 'ML_endtoend',
version = '0.0.1',
author = 'Rishi',
author_email = 'hrishikeshknair@gmail.com',
packages = find_packages(),
install_requires = get_requirments("requirements.txt")



)