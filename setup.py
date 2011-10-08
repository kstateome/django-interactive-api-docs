from setuptools import setup

version = '0.1.7'

setup(name='nuts-bolts-utils',
      version=version,
      description="Utilities for Django apps",
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT",
          ],
      keywords='django-utils',
      author='Derek Stegelman',
      author_email='dstegelman@gmail.com',
      url='http://github.com/dstegelman/nutsbolts-utils',
      license='MIT',
      packages=['nutsbolts', 'nutsbolts.utils', 'tagging', 'tagging.templatetags', 'tagging.migrations', 'tagging.tests'],
      install_requires = ['django==1.3'],
      include_package_data=True,
      zip_safe=True,
      )