from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
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
	msg_content = data["events"][0]["message"]
	print(data)
	reply_msg_content = {};

	if msg_type == "message":
	    message_reply(msg_replytoken, msg_source, msg_content)
	elif msg_type == "join":
		join_reply(msg_replytoken, msg_source)
	elif msg_type == "follow":
		follow_reply(msg_replytoken, msg_source)


	json_str = json.dumps(reply_msg_content)
	return "OK"

#reply function
def message_reply(replytoken, source, msg):
	print(source)
	print(msg)
	
	line_bot_api.reply_message(
		reply_token = replytoken,
		messages = [TextSendMessage(source["userId"] + msg["text"])]
		)
	
	pass	

def join_reply(replytoken, source):
	print(source)
	

def follow_reply(replytoken, source):
	print(source)
	