import requests
import re
import time
import sys
url = "https://app.squarespacescheduling.com/schedule.php?owner=22737217"
webhook = "https://discord.com/api/webhooks/1057397441072205904/l12FAQds6syHb3kiXiP7EW_dfD9qSt2w0nmY7eRziY6bIvfxI3apeHmhqFtFlhYkhEqm"

def send_webhook():
	message = "Check Site For Changes"
	payload = {
		"content": message
	}
	try:
		response = requests.post(webhook, json=payload)
		response.raise_for_status()
		print("Discord webhook message sent")
		sys.stdout.flush()
	except Exception as e:
		print(f"Error sending webhook: {e}")
		sys.stdout.flush()

target_element_text = 'NYE 30th'

delay = 1800
while True:
	response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"})
	if not re.search(target_element_text, response.text):
		print("Element is Missing Check For Changes")
		sys.stdout.flush()
		send_webhook()
	else:
		print("Element Present")
		sys.stdout.flush()
	time.sleep(delay)

