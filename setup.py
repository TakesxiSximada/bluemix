#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import (
    setup,
    find_packages,
    )

_here = os.path.dirname(os.path.abspath(__file__))


def here(path):
    return os.path.join(_here, path)

src = 'src'
install_requires = [line.strip() for line in open(here('requirements.txt'), 'rt')]
test_require = []
packages = find_packages(src)
package_dir = {'': src}
package_data = {}


setup(
    name='bluemix',
    version='0.1.0',
    url='https://github.com/TakesxiSximada/bluemix',
    download_url='https://github.com/TakesxiSximada/bluemix/archive/master.zip',
    license='See http://www.python.org/3.4/license.html',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="bluemix",
    long_description="bluemix",
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    packages=packages,
    package_dir=package_dir,
    namespace_packages=[
        ],
    package_data=package_data,
    include_package_data=True,
    install_requires=install_requires,
    test_require=test_require,
    entry_points='''
    [console_scripts]
    '''
    )
