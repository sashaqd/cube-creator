#!/bin/bash
set -e

# source env file if it exists
if [ -f .env ]; then
  source .env
fi

function sparql_update() {

    query=$1
    echo  "SPARQL UPDATE ${query}"

    response=$(
        curl \
            -v \
            --header "Content-Type: application/sparql-update; charset=UTF-8" \
            --data-binary "@${query}" \
            -u "${USER}:${PASSWORD}" \
            -o /dev/null \
            -w "%{http_code}" \
            "${ENDPOINT}/update"
    )

    echo "HTTP code: ${response}"
    if [[ $response != "200"  ]] && [[ $response != "204" ]]; then
        echo "FAILURE"
        message=$(
        curl \
            --header "Content-Type: application/sparql-update; charset=UTF-8" \
            --data-binary "@${query}" \
            -u "${USER}:${PASSWORD}" \
            "${ENDPOINT}/update"
        )
        echo $message
        exit 1
    fi
}

sparql_update "queries/remove_areas.rq"
sparql_update "queries/sum_vaccines.rq"
