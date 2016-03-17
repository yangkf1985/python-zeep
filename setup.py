from setuptools import find_packages, setup

install_requires = [
    'lxml>=3.0.0',
    'requests>=2.7.0',
    'six>=1.0.0',
]

tests_require = [
    'freezegun==0.3.6',
    'pytest-cov>=2.2.0',
    'pytest>=2.8.3',
    'requests_mock>=0.7.0',
]

setup(
    name='zeep',
    version='0.1.0',
    description='SOAP Client',
    url='http://www.python-zeep.org',
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',

    zip_safe=False,
)
