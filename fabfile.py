from __future__ import with_statement
from fabric.api import local, cd
import os
import glob


'''
    The following are build scripts for local development.
    We will include staging and production scripts later
    Author: Derek Stegelman
'''


def cleanup_compressed():
    # If you add more directories to compress, please add them in here so
    # that the built files get deleted on every build.
    try:
        local("cd assets/gating/css && rm *.min.css")
        local("cd assets/gating/secureit && rm *.min.js")
    except:
        pass

#def compress():

    #path = '_media/2011/js'
    #for file in glob.glob(os.path.join(path, '*.js')):
    #    basename, extension = os.path.splitext(file)
     #   local("java -jar compressor.jar -o %s.min.js %s" % (basename, file))

def sync_db():
    local("python manage.py syncdb --settings=settings.local")
    
def migrate():
    local("python manage.py migrate --settings=settings.local")
    
def pip_install():
    local("pip install -r requirements.txt")
    
def run_server():
    local("python manage.py runserver --settings=settings.local")

def tests():
    local("python manage.py test --settings=settings.local")

def build_migration(app):
    local("python manage.py schemamigration %s --auto --settings=settings.local" % app)
    

def run():
    pip_install()
    sync_db()
    migrate()
    #tests()
    #cleanup_compressed()
    #compress()
    run_server()
    
    
    