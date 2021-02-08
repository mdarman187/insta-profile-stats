from bs4 import BeautifulSoup
import requests

URL = "https://www.instagram.com/{}/"

def get_data(a):
  data = {}
  a = a.split("-")[0]
  a = a.split(" ")
  data['Followers'] = a[0]
  data['Following'] = a[2]
  data['Posts'] = a[4]
  return data

def scrape_data(username):
  b = requests.get(URL.format(username))
  a = BeautifulSoup(b.text, "html.parser")
  meta = a.find("meta", property = "og:description")
  return get_data(meta.attrs['content'])

if __name__ == "__main__":
  username = "mdarman_187"
  data = scrape_data(username)
  print(username,": has the following details.\n")
  print("This account has ",data["Followers"],"followers\n")
  print("This account has ",data["Following"],"following\n")
  print("This account has ",data["Posts"],"posts")
  

