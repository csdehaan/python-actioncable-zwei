from setuptools import find_packages, setup


setup(
    name='ActionCableZwei',
    version='1.2.0.0',
    license='MIT',
    description='Action Cable Client for Python 3',
    author='Tobias Feistmantl',
    author_email='tobias@myhome-automations.com',
    url='https://github.com/tobiasfeistmantl/python-actioncable-zwei',
    packages=find_packages(),
    install_requires=['websocket-client>=1.1.0']
)
