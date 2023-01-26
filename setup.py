import os
from screenctl import NAME, VERSION, DESCRIPTION
from setuptools import find_packages, setup


URL = 'https://github.com/QGrain/screenctl'
EMAIL = 'zhiyuzhang999@gmail.com'
AUTHOR = 'Zhiyu Zhang'

REQUIRED = [
    # 're', 'json'
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={
        'console_scripts': [
            'screenctl=screenctl.screenctl:main'
        ],
    },
    install_requires=REQUIRED,
    include_package_data = True,
    license='Apache-2.0',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)