
from setuptools import setup, find_packages

setup(
    name='my-insurance-scripts',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/CT2-DEVOPS-Team2/myinsurancescripts.git',
    author='Team2',
    author_email='myemail@example.com'
)


# twine upload --repository-url http://localhost:8081/repository/hosted-python/ dist/*