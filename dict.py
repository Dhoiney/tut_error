from bs4 import BeautifulSoup as BS
import requests
import re


class TutBy:
    __url = "https://news.tut.by/archive/{}.html"


# .rtop5 > div:nth-child(2) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1) > span:nth-child(1)

    def __init__(self, date: str):
        self.__news = {}
        self.__date = date


    # def get_page(self):
    #     root_page = requests.get(self.__url.format(self.__date))
    #     html = BS(root_page.text, features="html5lib")
    #     html = html.find("div", attrs={"id": "content-band"})
    #     html = html.find("div", attrs={"class": "l-columns"})
    #     b_news = html.find_all("div", attrs={"class": "b-news"})
    #     # print(len(b_news))

    def dict_creator(self):
        # a = {}
        root_page = requests.get(self.__url.format(self.__date))
        html1 = BS(root_page.text, features="html5lib")
        html1 = html1.find_all("span", attrs={"class": "entry-head _title"})
        text1 = str(html1)
        result = re.findall(r"<span.*?class:=[\"']*[\"']*.*?>(.*?)<\/span.*?>", text1)
        print(result)


    def __iter__(self):
        self.__cursor = 0
        return self


    def __next__(self):
        if self.__cursor < len(self.__news):
            try:
                return self.__news[self.__cursor]
            finally:
                self.__cursor += 1
        self.__cursor = 0
        raise StopIteration


if __name__ == "__main__":
    tut = TutBy("23.10.2020")
    # tut.parse()
    # for news in tut:
    #     print(news)
    # tut.get_page()
    tut.dict_creator()

