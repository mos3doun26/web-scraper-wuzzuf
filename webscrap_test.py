import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_text(lst):
    return [i.text for i in lst]

def scrap(page_link):
    respond = requests.get(page_link)
    soup = BeautifulSoup(respond.content, "lxml")

    titles = soup.find_all("h2", {"class": "css-m604qf"})
    links = [title.a["href"] for title in titles]
    job_types = soup.find_all("div", {"class": "css-1lh32fc"})
    campanies = soup.find_all("a", {"class": "css-17s97q8"})
    location = soup.find_all("span", {"class": "css-5wys0k"})

    data_fram = {
        "Title": get_text(titles),
        "Link": links,
        "Job Type": get_text(job_types),
        "Campany": get_text(campanies),
        "Location": get_text(location)
    }
    df = pd.DataFrame(data_fram)
    return df

if __name__ == "__main__":
    scrap(f"https://wuzzuf.net/search/jobs/?q=Machine%20learning&a=hpb")



