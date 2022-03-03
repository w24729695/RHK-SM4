from setuptools import setup, find_packages

setup(
    name='rhk-sm4',
    version='0.1.0',
    packages=find_packages(include=['rhk_sm4', 'rhk_sm4.*']),
    install_requires=[
        'numpy',
        'pandas'
    ],
    extras_require={
        'interactive': ['matplotlib', 'jupyter']    
        
    }
)

