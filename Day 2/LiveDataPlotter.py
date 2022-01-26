import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import CryptoClass
import time
import AudioClass

x = AudioClass.AudioPlayer(API_key='5130e857213c42939953cc81191b8dd8')
BTC = CryptoClass.CryptoRequestHandler('64c6dc2266249b9a2729eed0e22022dcd665cc6b27552c4da63665fd108f1b59')
BTC.get_price(crypto = 'BTC', currency = 'USD')

plt.style.use('seaborn-darkgrid')

x_values = []
y_values = []

index = count()


def animate(i):
    current_price = BTC.get_price('BTC', 'USD')
    current_price = current_price['BTC']['USD']
    i = next(index)
    if i%50 == 0:
        x.getTextToSpeech('Bitcoin price is : ' + str(current_price))

    x_values.append(i)
    y_values.append(current_price)
    plt.cla()
    plt.plot(x_values[-20:], y_values[-20:])
    # time.sleep(5)


ani = FuncAnimation(plt.gcf(), animate, 1000)


plt.tight_layout()
plt.show()