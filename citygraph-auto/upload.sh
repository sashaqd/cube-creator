#!/bin/bash

folder_path="file_generator/datasets"

# Iterate over subfolders
for subfolder in "$folder_path"/*; do
    if [ -d "$subfolder" ]; then
        subfolder_name=$(basename "$subfolder")
        
        # Iterate over files in the subfolder
        for file in "$subfolder"/*; do
            if [ -f "$file" ]; then
                file_name=$(basename "$file")
                
                # Run the file generator with file name as argument
                
                python3 file_generator/gen.py "$file"
                cp "$file" "input"
                mv test.csv.meta.json src-gen
                mv shape.ttl assets
                mv metadata.ttl assets

                npm run test
                rm "input/$file_name" 

                #curl https://citygraph.cluster-cdhplnwa3hlj.us-east-1.neptune.amazonaws.com:8182/sparql/gsp/?graph=urn:graph:$(cat abr.txt) -X POST -H 'Content-Type: text/turtle' --data-binary @output/place_holder.nt"
                #curl https://citygraph.cluster-cdhplnwa3hlj.us-east-1.neptune.amazonaws.com:8182/sparql/gsp/?graph=urn:graph:$(cat abr.txt) -X POST -H 'Content-Type: text/turtle' --data-binary @assets/metadata.ttl
                curl https://citygraph.cluster-cdhplnwa3hlj.us-east-1.neptune.amazonaws.com:8182/sparql/gsp/?graph=urn:graph:sasha -X POST -H 'Content-Type: text/turtle' --data-binary @output/place_holder.nt
                curl https://citygraph.cluster-cdhplnwa3hlj.us-east-1.neptune.amazonaws.com:8182/sparql/gsp/?graph=urn:graph:sasha -X POST -H 'Content-Type: text/turtle' --data-binary @assets/metadata.ttl
                
                rm abr.txt
            fi
        done
    fi
done



