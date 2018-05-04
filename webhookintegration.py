import requests, json, os, sys

class WebHookIntegration:
	def __init__(self):
		self.url = os.environ['WEBHOOK_URL']

	def _post(self, payload):
		r = requests.post(self.url, data=json.dumps(payload))
		return r
		
	def _validate_response(self, response):
		if response and response.status_code != 200:
			print("Invalid response. Error = %s" % str(response.body))
			return False
		return True
	
	def post_to_webhook(self, message):
		payload = {
			'text':message
		}
		print payload
		return self._post(payload)

def main(message):
	if len(message[1:]) != 1:
		print "Usage: only allowed arg is message to post!!"
		exit(1)
	webhookIntegration = WebHookIntegration()
	webhookIntegration.post_to_webhook(message[1:][0])

if __name__ == "__main__":
    main(sys.argv)
		

    
	
