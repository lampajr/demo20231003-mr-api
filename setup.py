import sys
from setuptools import setup, find_packages

NAME = "mr"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Model Registry gh44 draft",
    author_email="",
    url="",
    keywords=["OpenAPI", "Model Registry gh44 draft"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['mr=mr.__main__:main']},
    long_description="""\
    See also https://github.com/opendatahub-io/model-registry/issues/44#issue-1919724627
    """
)

