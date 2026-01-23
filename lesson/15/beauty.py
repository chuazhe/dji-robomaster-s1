import requests
from bs4 import BeautifulSoup
import random
import time


def fetch_and_parse(urls):
    for i in range(len(urls)):
        url = urls[i]
        print(f"Fetching URL {i+1}: {url}")
        try:
            response = requests.get(url)
            time.sleep(0.5)  
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = [tag.text for tag in soup.find_all('title')]
            print(f"Titles found: {titles}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")

num_urls = int(input("How many URLs do you want to fetch? "))
urls = []
for i in range(num_urls):
    url = input(f"Enter URL {i+1}: ")
    urls.append(url)

fetched = 0
while True:
    print(f"Fetching and parsing {num_urls} URLs...")
    fetch_and_parse(urls)
    fetched += 1
    time.sleep(1)
    if fetched >= 2:
        print("Fetched and parsed twice!")
        break
    else:
        print("Fetching again...")

index = 0
while index < num_urls:
    print(f"Index: {index}")
    index += 1
    if index > 3 and (index < num_urls or not(index == 5)):
        print(f"Special condition at index {index}")
else:
    print("Finished while-else loop.")


if urls:
    rand_idx = random.randint(0, len(urls)-1)
    if ("http" in urls[rand_idx] and len(urls[rand_idx]) > 10) or (urls[rand_idx].startswith("https")):
        print(f"URL {urls[rand_idx]} looks valid!")
    else:
        print("URL might be invalid.")
else:
    print("No URLs provided.")
