# plone52_buildout

Installationsprozedur für die Plone-Installationen der SIGUV-Kooperation

Installation
============

Vorbereitung des Ubuntu-Systems
-------------------------------

* sudo apt-get install build-essential python-dev libjpeg-dev libxslt-dev supervisor
* sudo apt-get install libpython3-dev
* sudo apt-get install python3-pip
* sudo apt-get install mongodb

Binaries zum Indexieren von Content
-----------------------------------

* sudo apt-get install wv
* sudo apt-get install poppler-utils

Vorbereitung und Durchführung des Plone-Buildouts
-------------------------------------------------

* ~ > git clone https://github.com/novareto/plone52_buildout.git $projectname
* ~ > cd $projectname
* ~/$projectname > python3 -m venv .
* ~/$projectname > ./bin/pip install -r requirements.txt
* ~/$projectname > ./bin/buildout

Buildout mit Developer-Tools
----------------------------
* ~/$projectname > ./bin/buildout -c develop.cfg

Anpassung der buildout.cfg nach git clone
-----------------------------------------

* user=admin:admin
* buildout-user = teamweb
* Portnummern der Clients
