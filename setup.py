from setuptools import setup, find_packages

setup(
    name='progressbar_utility',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'progressbar_test=progressbar_test:main',
        ],
    },
    author='DamianoLozzi',
    author_email='damianolozzi1989@gmail.com',
    description='A utility with a preconfigured progress bar',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DamianoLozzi/progress-bar',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)