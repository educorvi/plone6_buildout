import os
cwd = os.getcwd()

ploneversion = '5.2.9'
zopeversion = '4.8.2'

our = cwd + '/profiles/versions.cfg'
there = cwd + f'/profiles/{ploneversion}/'
versionfiles = [f'release-{ploneversion}-versions.cfg',
                f'version.cfg',
                f'Zope-releases-{zopeversion}-versions.cfg',
                f'Zope-releases-{zopeversion}-versions-prod.cfg']

def get_definitions(filedata):
    definitions = [i.replace('\n', '') for i in filedata.readlines() if not i.startswith('#') and not i.startswith('[') and i]
    return definitions

def get_versiondict(versionlist):
    versiondict = dict()
    for i in versionlist:
        if i:
            parts = i.split('=')
            try:
                versiondict[parts[0].strip()] = parts[1].strip()
            except:
                pass
    return versiondict

def compare(filename, ours, theres):
    resultlist = []
    for definition in ours:
        if definition in theres:
            if ours[definition] != theres[definition]:
                resultlist.append(f'{definition}: versions.cfg:{ours[definition]} {filename}:{theres[definition]}')
    return resultlist

ourfile = open(our, 'r')
ourdefinitions = get_definitions(ourfile)
ourversions = get_versiondict(ourdefinitions)
set1 = set(ourversions)

for i in versionfiles:
    therefile = open(there + i, 'r')
    theredefinitions = get_definitions(therefile)
    thereversions = get_versiondict(theredefinitions)
    results = compare(i, ourversions, thereversions)
    for i in results:
        print(i)
