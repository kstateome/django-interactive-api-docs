#Assumptions

* Python 2.7, PIP, and virtualenv installed.
* Use south
* Django 1.3 is the latest version of django at the current time.

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
    

