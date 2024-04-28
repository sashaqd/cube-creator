#first time - meta files

# curl -D- -H 'Content-Type: text/turtle' --upload-file meta_files/meta.nt -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:meta'
# curl -D- -H 'Content-Type: text/turtle' --upload-file meta_files/organization.nt -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:meta'


#repeated 

#data files
curl -D- -H 'Content-Type: text/turtle' --upload-file output/place_holder.nt -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:sasha'
curl -D- -H 'Content-Type: text/turtle' --upload-file assets/metadata.ttl -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:sasha'

#names
curl -D- -H 'Content-Type: text/turtle' --upload-file output/name.nt -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:main'

