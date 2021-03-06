import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession,AsyncHTMLSession
from selenium import webdriver
import time
import pathlib

def travel_kaohsiung_crawl():
	travel_kaohsiung_r = requests.get(
    "https://travel.ettoday.net/category/%E9%AB%98%E9%9B%84/")
	travel_soup = BeautifulSoup(travel_kaohsiung_r.text, "html.parser")
	travel_result_list = []

	travel_result = travel_soup.find_all(["h3"], attrs={"itemprop":"headline"})
	for travel_detail in travel_result:
		#print(travel_detail.getText() + " => ")
		#print(travel_detail.select_one("a").get("href"))
		travel_result_list.append(travel_detail.getText() + "link:"
			+ travel_detail.select_one("a").get("href"))

	#print(travel_result_list)
	return travel_result_list


def news_prove_crawl():
	news_prove_r = requests.get(
    "https://tfc-taiwan.org.tw/articles/report")
	news_soup = BeautifulSoup(news_prove_r.text, "html.parser")

	news_result = news_soup.find_all(["h3"], attrs={"class":"article-title"})

	return news_result

def cwb_crawl(cwb_page=1):
	cwb_local_url = "https://www.cwb.gov.tw"
	cwb_contents_url = ["/V8/C/W/OBS_Sat.html","/V8/C/W/OBS_Radar.html","/V8/C/P/Rainfall/Rainfall_QZJ.html"]
	cwb_search_url="";
	#choice which page to crawl
	if cwb_page >= 0 and cwb_page <= 2:
		cwb_search_url = cwb_contents_url[cwb_page]

	#set path to find webdriver
	file_path = pathlib.Path(__file__).parent.absolute()
	#print(str(file_path)+"\chromedriver")
	#set webdriver Options for dont show gui
	options = webdriver.ChromeOptions()
	options.add_argument("--headless")
	driver = webdriver.Chrome(str(file_path)+"\chromedriver" ,options=options)
	driver.get(cwb_local_url + cwb_search_url)
	htmlSource = driver.page_source
	cwb_soup = BeautifulSoup(htmlSource, "html.parser")
	cwb_soup = cwb_soup.find(["div"], attrs={"id":"link-1"})
	cwb_obs_img_url = cwb_soup.select_one("img").get("src")
	driver.quit()
	#===
	#print(cwb_local_url + cwb_obs_img_url)
	return cwb_local_url + cwb_obs_img_url
