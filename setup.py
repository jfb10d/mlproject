from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    :param file_path:
    :return:
    """
    requirements = []
    with open(file_path) as file:
        requirements=file.readlines()
    requirements = [req.replace('\n','') for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Jiaxin',
    author_email='fungkayan87@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)