from baselinker import Baselinker

API_TOKEN = '1011-10210-OYC7U14WRGM51M3WD5OKJ9TZPSO60MXQ09MJL92BGZ71Z0ME9DERL4INTVCTT3DS'


def run():
    # Create a baselinker client instance
    baselinker = Baselinker(API_TOKEN)
    # Prints 100 orders from baselinker
    print(baselinker.orders.get_orders())


if __name__ == '__main__':
    run()
