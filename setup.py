from setuptools import setup

setup(
    name='dmsmapgenerator',
    version='0.1.0',    
    description='This python tool generates a JSON file for the AWS DMS table mappings section.',
    url='https://github.com/emreoztoprak/dms-table-mapping-generator',
    author='Emre Öztoprak',
    author_email='e.oztoprak@yandex.com',
    license='MIT License',
    packages=setuptools.find_packages(where="./"),
    install_requires=['bullet==2.2.0',],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
