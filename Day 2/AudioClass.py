import requests
from playsound import playsound
from io import BytesIO

class AudioPlayer(object):

	def __init__(self, API_key, voice_info = None, hl = 'en-gb'):
		self.API_key = API_key
		self.voice_info = voice_info
		self.hl = hl
		self.URL = 'http://api.voicerss.org/'

	def getTextToSpeech(self, inputString):
		try:
			payLoad = {
						'key' : self.API_key,
						'hl'  : self.hl,
						'v' : self.voice_info,
						'src' : inputString
			}
			audioRequestObject = requests.get(url=self.URL, params=payLoad, timeout=10)
			file = open('output.wav', 'wb')
			file.write(audioRequestObject.content)
			file.close()
			playsound('output.wav')
		except Exception as e:
			raise e


if __name__ == '__main__':
	x = AudioPlayer(API_key='5130e857213c42939953cc81191b8dd8')
	x.getTextToSpeech('All we hear is, Radio Gaga')
		
