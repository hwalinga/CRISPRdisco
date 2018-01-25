from setuptools import setup

setup(
    name='crisprdisco',
    version='development',
    py_modules=[
    ],
    setup_requires =[
        "pytest-runner",
    ],
    tests_require=[
        "pytest==3.0.4",
    ],
    install_requires=[
        'pandas==0.19.1',
        'numpy==1.12.1',
        'matplotlib==1.5.1',
        'seaborn==0.7.1',
        'biopython==1.70',
        'click==6.7',
        'regex==2018.1.10',
    ],
    entry_points='''
        [console_scripts]
        disco=crisprdisco.cli.script:disco
    ''',
)

