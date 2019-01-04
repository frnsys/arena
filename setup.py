from setuptools import setup, find_packages

setup(
    name='arena',
    version='0.0.4',
    description='python interface to the are.na api',
    url='https://github.com/frnsys/arena',
    author='Francis Tseng (@frnsys)',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)