#!/bin/bash

folder_path="file_generator/datasets"
iterations_counter=1

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
                # mv test.csv.meta.json src-gen
                # mv shape.ttl assets
                mv metadata.ttl assets

                npm run test

                # Check the exit code
                # if [ $? -eq 0 ]; then
                #     echo "npm run test succeeded!"
                #     # Increment the iterations counter
                #     iterations_counter=$((iterations_counter + 1))
                # else
                #     echo "npm run test failed!"
                # fi

                rm "input/$file_name" 

                # curl -D- -H 'Content-Type: text/turtle' --upload-file output/place_holder.nt -X POST 'http://54.224.122.101:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:sasha'
                # curl -D- -H 'Content-Type: text/turtle' --upload-file assets/metadata.ttl -X POST 'http://54.224.122.101:9999/bigdata/namespace/wdq/sparql?context-uri=urn:graph:sasha'
                
                # rm abr.txt

                # if (( iterations_counter % 11 == 0 )); then
                #     read -p "Press Enter to continue to the next 10 iterations..."
                # fi
            fi
        done
    fi
done



