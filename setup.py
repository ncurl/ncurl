from setuptools import setup, find_packages

setup(
    name='nb-curl',
    version='0.1.2',
    keywords=('utils',),
    description='Next generation of curl',
    license='MIT License',
    install_requires=[],
    package_data={
        "app": []
    },
    author='bohan',
    author_email='bohanzhang@foxmail.com',
    entry_points={
        'console_scripts': [
            'nb-curl = app:main'
        ],
    },

    packages=find_packages(),
    scripts=['app.py'],
)