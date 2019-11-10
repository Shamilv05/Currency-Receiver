from setuptools import setup, find_packages

def parse_requirements(filename):
    """
    load requirements from a pip requirements file
    """
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

setup(
    name='CurrencyReciever',
    version='0.1dev',
    packages=find_packages(exclude=['tests']),
    license='MIT LICENSE',
    install_requires=parse_requirements('requirements.txt'),
    python_requires=">=3.6.0",
)
