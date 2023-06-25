#!/bin/bash

DATA_VERSION=$(curl -s 'https://www.covid19.admin.ch/api/data/context/history' | jq -r '.dataContexts[1].dataVersion')
wget "https://www.covid19.admin.ch/api/data/${DATA_VERSION}/downloads/sources-csv.zip"

# sudo apt-get install unzip
unzip -p sources-csv.zip data/COVID19AdministeredDoses_vaccine.csv > input/COVID19AdministeredDoses_vaccine.csv
unzip -p sources-csv.zip data/COVID19Cases_geoRegion.csv > input/COVID19Cases_geoRegion.csv
unzip -p sources-csv.zip data/COVID19Death_geoRegion.csv > input/COVID19Death_geoRegion.csv
unzip -p sources-csv.zip data/COVID19Hosp_geoRegion.csv > input/COVID19Hosp_geoRegion.csv
unzip -p sources-csv.zip data/COVID19VaccPersons_v2.csv > input/COVID19VaccPersons_v2.csv

npm run affected
./upload.sh PUT output/triples_affected.ttl

npm run vaccinated
./upload.sh POST output/triples_vaccinated.ttl

npm run vaccinedoses
./upload.sh POST output/triples_vaccinedoses.ttl

./upload.sh POST assets/dataset.ttl

./update.sh
