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
	    reply_msg_content = message_reply(msg_source, msg_content)
	elif msg_type == "join":
		reply_msg_content = join_reply(msg_source)
	elif msg_type == "follow":
		reply_msg_content = follow_reply(msg_source)

	line_bot_api.reply_message(
		reply_token = msg_replytoken,
		messages = TextSendMessage(reply_msg_content))

	json_str = json.dumps(reply_msg_content)
	return "OK"

#reply function
def message_reply(source, msg):
	print(source)
	print(msg)
	result_content = {}
	result_content["type"] = "text"
	result_content["text"] = source["userId"] + msg["text"]
	
	return result_content
	

def join_reply(source):
	print(source)
	

def follow_reply(source):
	print(source)
	