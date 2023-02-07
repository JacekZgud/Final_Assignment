import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FinalAssignment",
    version="1.0.0",
    author="Jacek Zgud",
    author_email="jacek.zgud2@gmail.com",
    description="Assignment package for Python in data science course",
    url="https://github.com/JacekZgud/Final_Assignment.git",
    packages=setuptools.find_packages(),
    install_requires=['pytest==6.2.4', 'numpy==1.24.1', 'pandas==1.5.3'],
    python_requires='>=3.6',
    )
