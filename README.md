= National Employment Register database for the 
== Ministry of Labour and Human Resource Development, Government of Kiribati

Software developed and written by Lachlan 'Musicman' Simpson (c)2012

Released under the GPL 3

Written using Django 1.4

South is installed:

Once a change has been made to app/models.py do this from within a virtualised
environment (otherwise django throws an error, as it uses the wrong django):
$ python manage.py schemamigration app --auto
then
$ python manage.py migrate app

Haystack is installed:
To add a new object model:
 - make appropriate changes to app/search_indexes.py
 - create mlhrd/ner/templates/search/indexes/ner/{model-name}_text.txt by coping 
 one that's already in there and making appropriate changes
 - map a new solr index:
    ./manage.py build_solr_schema > schema.xml
    cp schema.xml /opt/solr/solr/conf/ (dev laptop)
    cp schema.xml /home/solr/solr/solr/conf/ (prod server)

 - restart solr. In /etc/init/solr.conf it has a command to respawn the process 
 on unexpected termination, so something as simple as finding the process and 
 executing a kill -9 on it should be sufficient
 
 - Then build the new solr index:
    ./manage.py rebuild_index

