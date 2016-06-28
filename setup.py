from setuptools import setup

setup(
    name='travis_rpi_notif',
    version='0.0.1',
    description='Travis RaspberryPI Build Notifier',
    url='http://mena-devs.com',
    author='Bassem Dghaidi',
    author_email='bassem@interop.link',
    license='MIT',
    packages=['notifier'],
    install_requires=[
        'PyYAML',
        'travispy'
        'RPi.GPIO'
    ],
    zip_safe=False,
)
