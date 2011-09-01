#Overview

This application is based upon interactive API Docs from the Mashery.  Interactive docs allow your API consumers to see exactly
how your APIs are called and what results they should expect.  Take a look at api.stegelman.com for an example of how
this app is implemented.


##Assumptions/Requirement

* Python 2.7, PIP, and virtualenv installed.
* Use south
* Django 1.3 is the latest version of django at the current time.
* Documentation must reside on the same domain as the APIs in order to avoid cross-domain calls.

## Notes

This app includes a piece of middleware required for using jQuery with the PIP version of django-piston.  I have patched the core of django-piston so that
this is not required, but you'll need to download my version of django-piston here. https://github.com/dstegelman/django-piston/tree/develop-stable

I may begin distributing that version with this app if bug fixes continue to mount.

## Pip Requirements

* django==1.3
* south
* git+git://github.com/dstegelman/nutsbolts-utils.git

## General procedure 

Setup a new virtualenv::

    virtualenv appname --no-site-packages
    
Activate the virtualenv::
    
    source appname/bin/activate
    
Install the build requirement of fabric::

    pip install fabric

Add any vendor apps to requirements.txt.  You can remove django-piston and api-management if you aren't going to build an api.

Setup and run the environment::

    fab run
    

