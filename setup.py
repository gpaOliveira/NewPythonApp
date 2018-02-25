import os
from setuptools import setup,find_packages

project_name  =  "YourApp"
__version__  =  "1.0.0"
__author__  =  "Gabriel Oliveira"
__author_email__  =  "gabriel.pa.oliveira@gmail.com"
__author_username__  =  "gpaOliveira"
__description__  =  "Sample REST App with Flask"

#adapted from https://pythonhosted.org/an_example_pypi_project/setuptools.html
def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        pass
    return ""

setup(
    author = __author__,
    author_email = __author_email__,
    description = __description__,
    install_requires = read("requirements.txt"),
    license = read("LICENSE"),
    long_description = read("README.md"),
    name = project_name,
    packages = find_packages(),
    platforms = ["any"],
    test_suite = "nose2.collector.collector",
    url = "https://github.com/" + __author_username__ + "/" + project_name,
    version = __version__
)