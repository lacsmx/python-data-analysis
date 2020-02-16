from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()


setup(
    name='EMBL Open Targets',
    version='1.0.0',
    description='Access Open Targets Rest API',
    long_description=readme,
    author='Luis Cortés',
    author_email='luis.cortes.s.mx@gmail.com',
    url='https://www.linkedin.com/in/luiscs/',
    packages=find_packages(exclude=('tests', 'docs'))
)

