import easygui as e

price_list = []
#定义一个价格类
class Thing(object):
    def __init__(self, price, priceaddition, price_list):
        self.price = price
        self.priceaddition = priceaddition
        self.price_list = price_list
    def onprice(self, price, priceaddition, price_list):
        priceaddition = e.enterbox("请输入商品价格增长倍率>>")
        for i in range()
