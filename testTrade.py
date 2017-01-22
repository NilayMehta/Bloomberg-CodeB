import time
from company import *


companyArr = []

def trade():
    while True:
        for each in companyArr:
            update(each)
            buy(each)
            sell(each)
        time.sleep(2)
        
def buy(company):
    if company.shares == 0:
        company.price = company.currentBidPrice
        run("BID" + " " + company.name + " " + company.currentBidPrice  + " " + "1")
        print "Buy " + company.name
        run("MY_CASH")
        
def sell(company):
    if company.shares == 1 and company.currentAskPrice >= (company.price * 1.02):
        run("ASK" + " " + company.name + " " + company.currentAskPrice  + " " + "1")
        print "Sell " + company.name
        run("MY_CASH")
        company.reset()