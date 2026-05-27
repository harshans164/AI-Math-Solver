import serpapi
from pprint import pprint
import os 
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

#serpapi is not accurate and uses lot of tokens


def websearch_data(query):
  load_dotenv()
  client = serpapi.Client(api_key=os.environ.get("SERPER_API_KEY"))
  results = client.search({
    "engine": "google",
    "q": query
  })
  organic_results = results["organic_results"]

  info=""
  for index, page in enumerate(organic_results):
    if "youtube" not in page['link']:
      info+=str(index) + " . "
      info+=("Title : "+page['title']+"\n")
      url = page['link']
      r = requests.get(url)
      soup = BeautifulSoup(r.content, "html.parser")
      info+=("Body : "+soup.get_text())
      info+="\n"
      info+="==================================================================="
      info+="\n"
  return info


if __name__ == "__main__":
  print(websearch_data("newton's birthday"))