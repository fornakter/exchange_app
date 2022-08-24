from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import requests


class MainWdget(BoxLayout):
    default_value = '0'
    label1 = StringProperty('PLN')
    label2 = StringProperty('DOGE')
    label3 = StringProperty('TRX')
    label4 = StringProperty('BTC')
    label5 = StringProperty('ETH')

    def count_this(self):
        c = requests.get('https://api.cryptowat.ch/markets/prices')
        crypto_prices = c.json()

        # That code need to be corrected

        value_label = float(self.ids.value1.text)

        result_value = crypto_prices['result']['market:zonda:btcpln']
        result_value = value_label / result_value
        self.ids.value2.text = str(round(result_value, 8))

        result_value = crypto_prices['result']['market:zonda:trxpln']
        result_value = value_label / result_value
        self.ids.value3.text = str(round(result_value, 8))

        result_value = crypto_prices['result']['market:zonda:btcpln']
        result_value = value_label / result_value
        self.ids.value4.text = str(round(result_value, 8))

        result_value = crypto_prices['result']['market:zonda:ethpln']
        result_value = value_label / result_value
        self.ids.value5.text = str(round(result_value, 8))


class MainMenu(App):
    pass


if __name__ == '__main__':
    MainMenu().run()
