#!/bin/bash

# Blazegraph endpoint URL
ENDPOINT_URL="http://54.224.122.101:9999/bigdata/namespace/wdq/sparql"

# Extract the named graph from command-line arguments
GRAPH_NAME="$1"

# Check if the named graph is provided
if [ -z "$GRAPH_NAME" ]; then
    echo "Error: No named graph provided."
    echo "Usage: ./clear_graph.sh <graph-name>"
    exit 1
fi

# SPARQL query
SPARQL_QUERY="CLEAR GRAPH <$GRAPH_NAME>"

# Send the request
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "update=$SPARQL_QUERY" "$ENDPOINT_URL"