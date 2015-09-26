#!/usr/bin/python

import pycurl
import urllib
import json
from StringIO import StringIO

def getSentiment(text):

	response_buffer = StringIO()
	curl = pycurl.Curl()

	text_param = urllib.urlencode({'text': text})
	apikey_param = urllib.urlencode({'apikey': 'e6850c8b-8f13-456a-906c-bac391553fb2'})
	url = "https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?" + text_param + "&" + apikey_param + "&_=1443304026877"
	curl.setopt(curl.URL, url)

	curl.setopt(curl.WRITEFUNCTION, response_buffer.write)

	curl.perform()
	curl.close()

	response_value = response_buffer.getvalue()
	sentiment = json.loads(response_value)
	return sentiment["negative"][0]["score"]
