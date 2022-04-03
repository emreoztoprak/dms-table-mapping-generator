from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='dmsmapgenerator',
    version='0.1.0',    
    description='This python tool generates a JSON file for the AWS DMS table mappings section.',
    url='https://github.com/emreoztoprak/dms-table-mapping-generator',
    author='Emre Oztoprak',
    author_email='e.oztoprak@yandex.com',
    license='MIT License',
    #packages=['dmsmapgenerator'],
    install_requires=['bullet==2.2.0',],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
