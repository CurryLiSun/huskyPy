from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from huskyPy import app
from huskyPy.crawl.crawl_web import *

line_bot_api = LineBotApi("a8VhBE2YuovRR+T+qqCKW0r0NrRHxlM4XHapAA/N3RD4VHqXlbzVl5zJhBUJZqFI7AZtV+l6wBYoNuhY2+C2HiJ5gfKA6J/TX/YFrWUrlqD+2CzRnlrj5tSuKxhmOGN4JvjEcSKaONgaJCS8WOt1dQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("1501871c42abe646feb988e8cf56011e")

@app.route("/api_huskypy", methods=['POST'])
def api_huskypy():
	return "OK"