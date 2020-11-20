import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession,AsyncHTMLSession
import asyncio
loop = asyncio.get_event_loop()

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

async def cwb_crawl():
	cwb_local_url = "https://www.cwb.gov.tw"
	cwb_contents_url = ["/V8/C/W/OBS_Sat.html","/V8/C/W/OBS_Radar.html","/V8/C/P/Rainfall/Rainfall_QZJ.html"]
	cwb_img_contents_url = []

	#todo fix to Async
	asession = AsyncHTMLSession()
	r =await asession.get(cwb_local_url + cwb_contents_url[1])
	await r.html.arender()
	#r.html.render()
	rendered_js_attrs = r.html.find("div#link-1",first=True).html
	cwb_soup = BeautifulSoup(rendered_js_attrs, "html.parser")
	cwb_obs_result = cwb_soup.select_one("img").get("src")
	cwb_obs_img_url = cwb_obs_result

	for cwb_content in cwb_contents_url:
		#support js
		#session = HTMLSession()
		#r = session.get(cwb_local_url + cwb_content)
		#r.html.render()
		##===
		#rendered_js_attrs = r.html.find("div#link-1",first=True).html
		#cwb_soup = BeautifulSoup(rendered_js_attrs, "html.parser")
		#cwb_obs_result = cwb_soup.select_one("img").get("src")
		#cwb_obs_img_url = cwb_obs_result

		#cwb_img_contents_url.append(cwb_obs_img_url)
		##print(cwb_local_url + cwb_obs_img_url)
		pass

	print(cwb_obs_img_url)
	return cwb_obs_img_url
