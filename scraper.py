import requests
from bs4 import BeautifulSoup
import os

# Base URL of the website to scrape
base_url = 'https://admin.bayanat.ae/home/datasets?langKey=en'

# Path to the folder where downloaded data sets will be saved
save_folder = '/Users/sasha/desktop/bayanat_data'

# Number of pages to scrape
num_pages = 1

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Loop through each page
for page in range(1, num_pages+1):

    # Construct the URL of the page to scrape
    url = base_url #+ f'page/{page}/'

    # Make a GET request to the page with all data sets
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the topics with links to data sets
    topics = soup.select('.kt-widget4__username')

    # Loop through all topics
    for topic in topics:

        topic_name = topic.text.strip()
        file_path = save_folder
        file_path = file_path + "/" + topic_name
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        print(f'Downloading data sets for {topic_name}...')

        # Get the URL of the page with the links to data sets
        topic_url = 'https://admin.bayanat.ae' + topic['href']

        # Make a GET request to the page with the links to data sets
        response = requests.get(topic_url)

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)
        # Find the links to each data set

        divs = soup.find_all("a", class_="btn btn-label-primary btn-bold btn-sm btn-icon-h kt-margin-l-10 download-btn-rsrc")
        nameList = soup.find_all("div", class_="kt-widget4__item")

        names = []
        for name in nameList:
            title = name.find("a", class_="kt-widget4__title")
            if title is not None:
                #print(title.text.strip())
                names.append(title.text.strip())


        # extract the href value from each div element that contains an <a> tag
        links = []
        for div in divs:
            #print('https://admin.bayanat.ae' + div['href'])
            links.append('https://admin.bayanat.ae' + div['href'])

        # Loop through each data set and download it
        for i in range (0,len(links)):
            # Get the name of the data set from the link text
            name = names[i]
            # Get the URL of the data set from the link href attribute
            url = links[i]

            # Download the data set and save it to the specified folder
            new_file_path = os.path.join(file_path, name)
            if not os.path.exists(new_file_path):
                print(f'Downloading {name}...')
                response = requests.get(url)
                with open(new_file_path, 'wb') as f:
                    f.write(response.content)
                print(f'{name} downloaded successfully.')
            else:
                print(f'{name} already exists in {file_path}. Skipping download.')
