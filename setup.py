import os
import re
import sys
from setuptools import setup, find_packages


def version_read():
    settings_file = open(os.path.join(os.path.dirname(__file__), 'lib', 'shellescape', 'settings.py')).read()
    major_regex = r"""major_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    minor_regex = r"""minor_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    patch_regex = r"""patch_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    major_match = re.search(major_regex, settings_file)
    minor_match = re.search(minor_regex, settings_file)
    patch_match = re.search(patch_regex, settings_file)
    major_version = major_match.group(1)
    minor_version = minor_match.group(1)
    patch_version = patch_match.group(1)
    if len(major_version) == 0:
        major_version = 0
    if len(minor_version) == 0:
        minor_version = 0
    if len(patch_version) == 0:
        patch_version = 0
    return major_version + "." + minor_version + "." + patch_version


# Use repository Markdown README.md for PyPI long description
try:
    with open("README.md", "r") as f:
        readme = f.read()
except IOError as readme_e:
    sys.stderr.write(
        "[ERROR] setup.py: Failed to read the README.md file for the long description definition: {}".format(
            str(readme_e)
        )
    )
    raise readme_e


setup(
    name='shellescape',
    version=version_read(),
    description='Shell escape a string to safely use it as a token in a shell command (backport of cPython shlex.quote for Python versions 2.x & < 3.3)',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/chrissimpkins/shellescape',
    license='MIT license',
    author='Christopher Simpkins',
    author_email='git.simpkins@gmail.com',
    platforms=['any'],
    packages=find_packages("lib"),
    package_dir={'': 'lib'},
    keywords='shell,quote,escape,backport,command line,command,subprocess',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows'
    ],
)
