import requests

class CryptoRequestHandler():
	def __init__(self, API_key):
		self.API_key = API_key
		self.URL = 'https://min-api.cryptocompare.com/data/'


	def get_price(self, crypto, currency):
		try:
			callType, cryptoCall = 'price', 'fsym'
			if type(currency) is not list:
				temp_list = []
				temp_list.append(currency)
				currency = temp_list

			if type(crypto) is not list:
				temp_list = []
				temp_list.append(crypto)
				crypto = temp_list

			if len(currency) > 1 or len(crypto):
				callType = 'pricemulti'
				cryptoCall = 'fsyms'

			payload = {
						'api_key' : self.API_key,
						cryptoCall    : crypto,
						'tsyms'   : ','.join(currency)
					}
			get_price_object = requests.get(url=self.URL+callType, params=payload).json()
			return get_price_object
		except Exception as e:
			raise e

if __name__ == '__main__':
	BTC = CryptoRequestHandler('64c6dc2266249b9a2729eed0e22022dcd665cc6b27552c4da63665fd108f1b59')
	print(BTC.get_price(crypto = 'BTC', currency = 'USD')['BTC']['USD'])



	