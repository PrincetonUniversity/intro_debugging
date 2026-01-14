# Pre-Workshop Local Install Directions

This guide will help you setup your local environment for participating in the hands on exercises for **Debugging and Profiling Code in Python**. The workshop will show participants how to use commandline and Visual Syudio Code debugger for Python.  workshop will also cover profiling of Python code.

To participate in the hands-on lessons one will need:

- A laptop with sufficient battery power. 
- Local install of Git, Miniconda and Visual Studio Code.
OR
- Remote access using OnDemand is available for users with a Princeton Net ID account and access to Adroit teaching cluster.     
- Create a conda environment using the environment.yml.

## Locally Install Required Tools

Please follow the instructions below to install the tools required for the hands-on exercises. The tools are available for all 3
major operating systems, and the appropriate versions should be downloaded and installed.

### Local Install of Miniconda

Anaconda is a package and environment manager commonly used for python. However, it is very large and has lot of packages not necessary for this workshop. If you have Anaconda installed already please skip this step.

Otherwise, follow the steps in the link below to install miniconda a smaller lighweight install with just necessary packages. 

https://www.anaconda.com/docs/getting-started/miniconda/install

### Local Install of Git

Git is a code repository tool that we will use to download all the code files for the workshop. Follow the instructions below to install Git:

https://git-scm.com/install

### Create Conda Environment

1. Open the commandline interface of your operating system. 
2. Use the command ```git clone https://github.com/PrincetonUniversity/intro_debugging.git``` to download the code repository
3. Navigate to the directory where the environment.yml is saved: ```cd  intro_debugging/00_install```
4. Run command to install required environment: ```conda env create -f environment.yml```


### Local Install of Visual Studio Code

## Remote Access to Adroit

If you prefer not to locally install anything please follow the steps in the link below to check if you have access to Adroit and request access if needed. 

https://researchcomputing.princeton.edu/systems/adroit#How-to-Access-the-Adroit-Cluster 

### Install the Conda Environment on Adroit 

1. Login to https://myadroit.princeton.edu 
2. Go to the ```Clusters``` tab and click on the ```Adroit Cluster Shell Access``` menu
3. Use the command ```git clone https://github.com/PrincetonUniversity/intro_debugging.git``` to download the code repository
4. Navigate to the directory where the environment.yml is saved: ```cd  intro_debugging/00_install```
5. Load the anaconda module: ```module load anaconda3/2025.12```
5. Run command to install required environment: ```conda env create -f environment.yml```


