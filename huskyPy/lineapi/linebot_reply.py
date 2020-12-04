from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from huskyPy import app
from huskyPy.crawl.crawl_web import *
from flask import request
import json

line_bot_api = LineBotApi("a8VhBE2YuovRR+T+qqCKW0r0NrRHxlM4XHapAA/N3RD4VHqXlbzVl5zJhBUJZqFI7AZtV+l6wBYoNuhY2+C2HiJ5gfKA6J/TX/YFrWUrlqD+2CzRnlrj5tSuKxhmOGN4JvjEcSKaONgaJCS8WOt1dQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("1501871c42abe646feb988e8cf56011e")

@app.route("/api_huskypy", methods=['POST'])
def api_huskypy():
	data = request.json
	msg_type = data["events"][0]["type"]
	msg_replytoken = data["events"][0]["replyToken"]
	msg_source = data["events"][0]["source"]
	print("===req data")
	print(data)
	reply_msg_content = {};

	if msg_type == "message":
		msg_content = data["events"][0]["message"]
		message_reply(msg_replytoken, msg_source, msg_content)
	elif msg_type == "join":
		join_reply(msg_replytoken, msg_source)
	elif msg_type == "follow":
		follow_reply(msg_replytoken, msg_source)

	json_str = json.dumps(reply_msg_content)
	return "OK"

#reply function
def message_reply(replytoken, source, msg):
	no_space_msg = str(msg["text"]).lstrip().rstrip()
	result_search = None
	#remove string head and foot space
	if no_space_msg == "@雷達":
		result_search = cwb_crawl(1)

		line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [ImageSendMessage(original_content_url=result_search,
							   preview_image_url=result_search)]
		)

	elif no_space_msg == "@衛星":
		result_search = cwb_crawl(0)

		line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [ImageSendMessage(original_content_url=result_search,
							   preview_image_url=result_search)]
		)
	elif no_space_msg == "@雨量":
		result_search = cwb_crawl(2)

		line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [ImageSendMessage(original_content_url=result_search,
							   preview_image_url=result_search)]
		)
	elif no_space_msg == "@高雄旅遊":
		result_search = travel_kaohsiung_crawl()

		line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [TextSendMessage(str(result_search))]
		)
	elif no_space_msg == "@新聞真假":
		result_search = news_prove_crawl()

		line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [TextSendMessage(result_search)]
		)
	elif no_space_msg == "@加油打氣":
		result_search = "加油，這並不容易，不過我們全體PUA都會支持你!"

		line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [TextSendMessage(result_search)]
		)
		pass
	
	pass

def join_reply(replytoken, source):
	#welcome join my line bot
	msg_send = "感謝加入，目前服務以下 \n \
				1.氣象查詢服務(輸入:@雷達,@衛星,@雨量) \n \
				2.旅遊資訊服務(輸入:@高雄旅遊) \n \
				3.旅遊資訊服務(輸入:@新聞真假) \n"
	line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [TextSendMessage(msg_send)]
		)

def follow_reply(replytoken, source):
	#welcome follow my line bot
	msg_send = "感謝您的加入，目前服務有以下 \n \
				1.氣象查詢服務(輸入:@雷達,@衛星,@雨量) \n \
				2.旅遊資訊服務(輸入:@高雄旅遊) \n \
				3.旅遊資訊服務(輸入:@新聞真假) \n"
	line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [TextSendMessage(msg_send)]
		)
	