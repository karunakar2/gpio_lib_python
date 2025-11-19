"""
Copyright (c) 2012-2015 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
'''
from distutils.core import setup, Extension

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(name             = 'ASUS.GPIO',
      version          = '0.1',
      author           = 'ASUS',
      author_email     = 'ASUS@asus.com',
      description      = 'A module to control ASUS GPIO channels',
      long_description = open('README.txt').read() + open('CHANGELOG.txt').read(),
      license          = 'MIT',
      keywords         = 'ASUS GPIO',
      url              = 'https://github.com/TinkerBoard/gpio_lib_python',
      classifiers      = classifiers,
      packages         = ['ASUS'],
      ext_modules      = [Extension('ASUS.GPIO', ['source/py_gpio.c', 'source/c_gpio.c', 'source/cpuinfo.c', 'source/event_gpio.c', 'source/soft_pwm.c', 'source/py_pwm.c', 'source/common.c', 'source/constants.c', 'source/wiringTB.c'])])

setup(name             = 'RPi.GPIO',
      version          = '0.1',
      author           = 'ASUS',
      author_email     = 'ASUS@asus.com',
      description      = 'A module to control ASUS GPIO channels',
      long_description = open('README.txt').read() + open('CHANGELOG.txt').read(),
      license          = 'MIT',
      keywords         = 'ASUS GPIO',
      url              = 'https://github.com/TinkerBoard/gpio_lib_python',
      classifiers      = classifiers,
      packages         = ['RPi'],
      ext_modules      = [Extension('RPi.GPIO', ['source/py_gpio_RPi.c', 'source/c_gpio.c', 'source/cpuinfo.c', 'source/event_gpio.c', 'source/soft_pwm.c', 'source/py_pwm.c', 'source/common.c', 'source/constants.c', 'source/wiringTB.c'])])
'''

from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
readme = ""
if (this_dir / "README.md").exists():
    readme = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="gpio_lib_python",
    version="0.0.1",
    description="GPIO helper library (updated for Python 3)",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="(original author)",
    license="MIT",
    packages=find_packages(where="."),
    include_package_data=True,
    install_requires=[
        # Add runtime deps here if needed, e.g. "RPi.GPIO>=0.7" as an extra.
    ],
    extras_require={
        "rpi": ["RPi.GPIO>=0.7"],
        "gpiod": ["gpiod"],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
