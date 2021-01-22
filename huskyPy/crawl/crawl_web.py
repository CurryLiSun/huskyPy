import os
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession,AsyncHTMLSession
from selenium import webdriver
import time
import pathlib

def travel_kaohsiung_crawl():
	#define res data member
	travel_result_list = []
	travel_kaohsiung_r = requests.get(
    "https://travel.ettoday.net/category/%E9%AB%98%E9%9B%84/")
	travel_soup = BeautifulSoup(travel_kaohsiung_r.text, "html.parser")

	travel_result = travel_soup.find_all(["h3"], attrs={"itemprop":"headline"})
	for travel_detail in travel_result:
		#print(travel_detail.getText() + " => ")
		#print(travel_detail.select_one("a").get("href"))
		travel_result_list.append(travel_detail.getText() + "\n"
			+"詳細連結:"
			+ travel_detail.select_one("a").get("href") + "\n"
		)

	covernt_str = "".join(travel_result_list)
	#print(travel_result_list)
	return covernt_str


def news_prove_crawl():
	#define res data member
	news_result_list = []
	source_url = "https://tfc-taiwan.org.tw"
	news_prove_r = requests.get(
    "https://tfc-taiwan.org.tw/articles/report")
	news_soup = BeautifulSoup(news_prove_r.text, "html.parser")

	news_result = news_soup.find_all(["h3"], attrs={"class":"entity-list-title"})
	for news_detail in news_result:
	    news_result_list.append(news_detail.getText() + "\n"
			+"詳細連結:"
			+ source_url+news_detail.select_one("a").get("href") + "\n\n"
		)

	covernt_str = "".join(news_result_list)
	return covernt_str

def joke_crawl():
	#define res data member
	travel_result_list = []
	travel_kaohsiung_r = requests.get(
    "https://www.xiaohuayoumo.com/")
	travel_soup = BeautifulSoup(travel_kaohsiung_r.text, "html.parser")

	return travel_soup

def cwb_crawl(cwb_page = 1):
	cwb_local_url = "https://www.cwb.gov.tw"
	cwb_contents_url = ["/V8/C/W/OBS_Sat.html","/V8/C/W/OBS_Radar.html","/V8/C/P/Rainfall/Rainfall_QZJ.html"]
	cwb_search_url="";
	#choice which page to crawl
	if cwb_page >= 0 and cwb_page <= 2:
		cwb_search_url = cwb_contents_url[cwb_page]

	#set path to find webdriver
	#file_path = pathlib.Path(__file__).parent.absolute()
	#print(str(file_path)+"\chromedriver")
	#set webdriver Options for dont show gui
	options = webdriver.ChromeOptions()
	options.add_argument("--headless")
	options.add_argument("--disable-dev-shm-usage")
	options.add_argument("--no-sandbox")
	options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	#print(os.environ.get("GOOGLE_CHROME_BIN") is not None)
	print(os.environ)
	#when evniron BIN PATH no value, then defult local PATH
	#for cloud system server use
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH" ,"chromedriver"), chrome_options=options)
	if os.environ.get("GOOGLE_CHROME_BIN") is not None :
	    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
	#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
	#for windows system server use
	#driver = webdriver.Chrome("chromedriver" ,options=options)
	#for linux system server use
	#driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver" ,options=options)
	driver.get(cwb_local_url + cwb_search_url)
	htmlSource = driver.page_source
	cwb_soup = BeautifulSoup(htmlSource, "html.parser")
	cwb_soup = cwb_soup.find(["div"], attrs={"id":"link-1"})
	cwb_obs_img_url = cwb_soup.select_one("img").get("src")
	driver.quit()
	#===
	#print(cwb_local_url + cwb_obs_img_url)
	return cwb_local_url + cwb_obs_img_url
