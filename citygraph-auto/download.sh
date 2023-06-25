#!/bin/bash
DATA_VERSION=$(curl -s 'https://www.covid19.admin.ch/api/data/context/history' | jq -r '.dataContexts[1].dataVersion')
wget "https://www.covid19.admin.ch/api/data/${DATA_VERSION}/downloads/sources-csv.zip"
unzip -p sources-csv.zip data/COVID19AdministeredDoses_vaccine.csv > input/COVID19AdministeredDoses_vaccine.csv
unzip -p sources-csv.zip data/COVID19Cases_geoRegion.csv > input/COVID19Cases_geoRegion.csv
unzip -p sources-csv.zip data/COVID19Death_geoRegion.csv > input/COVID19Death_geoRegion.csv
unzip -p sources-csv.zip data/COVID19Hosp_geoRegion.csv > input/COVID19Hosp_geoRegion.csv
unzip -p sources-csv.zip data/COVID19VaccPersons_v2.csv > input/COVID19VaccPersons_v2.csv
