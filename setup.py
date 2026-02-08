import setuptools
from distutils.core import setup

setup(
    name='task-tracker-cli',
    version='0.0.0',
    description='Task Tracker CLI',
    author='Jiehoon Lee',
    author_email='jiehoonn@bu.edu',
    packages=['cli_folder'],
    entry_points={
        'console_scripts': ['task-cli=cli_folder.entry:cli_entry_point'],
    },
    install_requires=[
        'tabulate',
    ],
)