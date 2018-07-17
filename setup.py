from setuptools import setup, find_packages

setup(
    name='crisprdisco',
    version='development',
    packages=find_packages(),
    py_modules=[
    ],
    setup_requires =[
    ],
    tests_require=[
    ],
    install_requires=[
        'pandas==0.23.1',
        'numpy==1.14.5',
        'biopython==1.69',
        'click==6.7'
    ],
    entry_points='''
        [console_scripts]
        disco=crisprdisco.cli.script:disco
    ''',
)

