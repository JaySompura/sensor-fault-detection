#from tkinter.ttk import setup_master
from typing import List
from setuptools import find_packages, setup
from typing import List

#def get_requirements()->List[str]:
"""
    This function will return list of requirement from requirements.txt files.
    """
    #requirement_data:object = open("requirements.txt","r")
    #data:str = requirement_data.read()
    #requirement_list:list[str] = list(data.split("\n"))
    #print(requirement_list)
    #return requirement_list 


setup(
    name="sensor",
    version="0.0.1",
    author="Jay Sompura",
    author_email="jaynsompura20@gmail.com",
    packages=find_packages(),
    #install_requires=get_requirements(),
)