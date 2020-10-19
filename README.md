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

Referenzsysteme
---------------

Basic-Auth für alle Referenzsysteme:

Benutzername: plone
Passwort: uvc

Die Plone-Referenzsysteme werden auf dem folgendem Server bei der BG-Verkehr gehostet: 10.33.204.103

/home/siguv:

* plone52_max = maximale Konfig (plonetheme.siguv)
* plone52_min = minimale Konfig (plonetheme.tokyo)
* plone52_dev = Development (plonetheme.siguv + jeweils neue Plone-Version)

Ports:

* 8080 = maximale Konfig (plonetheme.siguv)
* 8090 = minimale Konfig (plonetheme.tokyo)
* 8070 = Development (plonetheme.siguv + jeweils neue Plone-Version) 

Externe URLs:

* plone.bg-kooperation.de = maximale Konfig (aktuelle Referenz-Konfiguration)
* plone-min.bg-kooperation.de = minimale Plone-Konfiguration (plonetheme.tokyo)
* plone-dev.bg-kooperation.de = maximale Konfig + neue Plone-Version

Ansprechpartner
---------------
- Lars Walther (lwalther@novareto.de)
- Miriam Dünnwald (duennwald.miriam@bgetem.de)

- fachlich: Holger Zingsheim (BG ETEM)

Maintainer
----------

- Miriam Dünnwald (duennwald.miriam@bgetem.de)