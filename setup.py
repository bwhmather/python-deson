from setuptools import setup, find_packages


setup(
    name='deson',
    url='https://github.com/bwhmather/python-deson',
    version='0.0.1',
    author='Ben Mather',
    author_email='bwhmather@bwhmather.com',
    maintainer='',
    license='BSD',
    description=(
        "A library for building parsers for json data"
    ),
    long_description=__doc__,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
    ],
    packages=find_packages(),
    package_data={
        '': ['*.*'],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    test_suite='deson.tests.suite',
)
