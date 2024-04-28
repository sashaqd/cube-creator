#!/bin/bash

list_folders() {
    for entry in "$1"/*; do
        if [ -d "$entry" ]; then
            placeholder_path="$entry/place_holder.nt"
            name_path="$entry/name.nt"
            metadata_path="$entry/metadata.ttl"

            # You can add commands here to do something with the paths
            echo "Placeholder path: $placeholder_path"
            echo "Name path: $name_path"
            echo "Metadata path: $metadata_path"
            curl -D- -H 'Content-Type: text/turtle' --upload-file $placeholder_path -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:sasha'
            curl -D- -H 'Content-Type: text/turtle' --upload-file $metadata_path -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:sasha'
            curl -D- -H 'Content-Type: text/turtle' --upload-file $name_path -X POST 'http://10.230.240.198:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:main'

        fi
    done
}

# Specify the path to list folders from
root_path="/Users/sasha/desktop/temp"

# List all folders in the specified path
list_folders "$root_path"
