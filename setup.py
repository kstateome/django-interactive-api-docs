from setuptools import setup, find_packages

version = '1.2dev'

setup(name='django-api-docs',
      version=version,
      description="Interactive API Documentation",
      long_description=open("README.md", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='django-interactive-api-docs',
      author='Derek Stegelman',
      author_email='dstegelman@gmail.com',
      url='http://github.com/dstegelman/django-interactive-api-docs',
      license='MIT',
      packages=find_packages(),
      install_requires = ['hadrian==1.1.3', 'suds==0.4'],
      include_package_data=True,
      zip_safe=False,
    )
