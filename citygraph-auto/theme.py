# themes = ["AbuDhabiAgricultureAndFoodSafetyAuthority","AlJazeeraPort","CentralBankofUnitedArabEmirates","DepartmentofHealth-AbuDhabi","DubaiPulse","EmiratesPostGroup","EtihadWaterandElectricity","FederalAuthorityForGovernmentHumanResource","FederalAuthorityForIdentityandCitizenship","FederalAuthorityForNuclearRegulation","FederalCompetitivenessandStatisticsCenter","FederalCustomsAuthority","FederalTransportAuthority-Land&Maritime","GeneralAuthorityofCivilAviation","GeneralAuthorityofIslamicAffairsandEndowments","GeneralPension&SocialSecurityAuthority","GovernmentofFujairah","HigherCollegesofTechnology","InsuranceAuthority","MinistryOfClimateChange&Environment","MinistryofCommunityDevelopment","MinistryofCulture&KnowledgeDevelopment","MinistryOfEconomy","MinistryofEducation","MinistryOfEnergy&Industry","MinistryofEnergy&Infrastructure","MinistryofFinance","MinistryofForeignAffairsandInternationalCooperation","MinistryofHealthandPrevention","MinistryOfHumanResources&Emiratizations","MinistryofIndustryandAdvancedTechnology","MinistryOfInterior","MinistryofJustice","MinistryofStateforFederalNationalCouncilAffairs","Municipality&PlanningDepartment-Ajman","NationalMediaCouncil","NationalQualificationAuthority","RasAlKhaimahMaritimeCity","RoadsandTransportAuthority","SecuritiesandCommoditiesAuthority","ShaikhZayedHousingProgramme","StatisticsCentre−AbuDhabi","TelecommunicationsandDigitalGovernmentRegulatoryAuthority","UnitedArabEmiratesSpaceAgency","UnitedArabEmiratesUniversity","ZakatFund","ZayedUniversity"]
# themes1 = ["Abu Dhabi Agriculture And Food Safety Authority","Al Jazeera Port","Central Bank of United Arab Emirates","Department of Health - Abu Dhabi","Dubai Pulse","Emirates Post Group","Etihad Water and Electricity","Federal Authority For Government Human Resource","Federal Authority For Identity and Citizenship","Federal Authority For Nuclear Regulation","Federal Competitiveness and Statistics Center","Federal Customs Authority","Federal Transport Authority - Land & Maritime","General Authority of Civil Aviation","General Authority of Islamic Affairs and Endowments","General Pension & Social Security Authority","Government of Fujairah","Higher Colleges of Technology","Insurance Authority","Ministry Of Climate Change & Environment","Ministry of Community Development","Ministry of Culture & Knowledge Development","Ministry Of Economy","Ministry of Education","Ministry Of Energy & Industry","Ministry of Energy & Infrastructure","Ministry of Finance","Ministry of Foreign Affairs and International Cooperation","Ministry of Health and Prevention","Ministry Of Human Resources & Emiratizations","Ministry of Industry and Advanced Technology","Ministry Of Interior","Ministry of Justice","Ministry of State for Federal National Council Affairs","Municipality & Planning Department - Ajman","National Media Council","National Qualification Authority","Ras Al Khaimah Maritime City","Roads and Transport Authority","Securities and Commodities Authority","Shaikh Zayed Housing Programme","Statistics Centre − Abu Dhabi","Telecommunications and Digital Government Regulatory Authority","United Arab Emirates Space Agency","United Arab Emirates University","Zakat Fund","Zayed University"]

# list1 = []
# list2 = []
# list3 = []
# list4 = []
# list5 = []
# for theme, t in zip(themes, themes1):
#     list1.append("<https://citygraph.co/opendata/"+theme+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Organization> .")
#     list2.append("<https://citygraph.co/opendata/"+theme+"> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/DefinedTerm> .")
#     list3.append("<https://citygraph.co/opendata/"+theme+"> <http://schema.org/name> \""+t+"\"@en .")
#     list4.append("<https://citygraph.co/opendata/"+theme+"> <http://schema.org/description> \""+t+"\"@en .")
#     list5.append("<https://citygraph.co/opendata/"+theme+"> <http://schema.org/inDefinedTermSet> <https://register.ld.admin.ch/opendataswiss/org> .")
    

# for l1 in list1:
#     print(l1)
# for l2 in list2:
#     print(l2)
# for l3 in list3:
#     print(l3)
# for l4 in list4:
#     print(l4)
# for l5 in list5:
#     print(l5)


import csv

def create_dataset_dictionary(csv_file_path):
    dataset_dict = {}
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            attribute_type = row[0]
            attribute_name = row[1]

            for dataset in row[2:]:
                if dataset not in dataset_dict:
                    dataset_dict[dataset] = {}
                    dataset_dict[dataset]["theme"] = []
                    dataset_dict[dataset]["organization"] = []
                    dataset_dict[dataset]["goal"] = []
                
                dataset_dict[dataset][attribute_type].append(attribute_name)
    return dataset_dict

# Specify the path to your CSV file
csv_file_path = '/Users/sasha/desktop/bayanat/otherMetadata.csv'
# Call the function to create the dataset dictionary
dataset_dictionary = create_dataset_dictionary(csv_file_path)

# Print the dataset dictionary
for dataset, attributes in dataset_dictionary.items():
    print("Dataset:", dataset)
    print("Attributes:")
    for attribute_type, attribute_name in attributes.items():
        print("- Type:", attribute_type)
        print("- Name:", attribute_name)
    print()


