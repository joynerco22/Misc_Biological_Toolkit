from setuptools import setup, find_packages

setup(
    name='Misc_Biological_Toolkit',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'biopython',
    ],
    entry_points='''
        [console_scripts]
        my_toolkit=my_toolkit.cli:cli
    ''',
    author="Cory Joyner",
    author_email="coryjoyner526@gmail.com",
    description="A basic command line toolkit incorporating helpful scripts I accumulated as a grad student, wrapped together in a package",
    url="https://github.com/yourusername/my_toolkit",
)