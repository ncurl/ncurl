from setuptools import setup, find_packages

setup(
    name='ncurl',
    version='0.4.1',
    keywords=('utils', 'curl',),
    description='Next generation of curl',
    license='MIT License',
    install_requires=['Pygments', 'uncurl', 'requests', 'setuptools'],
    include_package_data=True,
    zip_safe=True,
    author='bohan',
    author_email='bohanzhang@foxmail.com',
    entry_points={
        'console_scripts': [
            'ncurl = ncurl.app:main'
        ],
    },

    packages=find_packages(),
)