import socket
import sys
import csv
import json
import time
import os
from company import *

user = "algorhythms"
password = "nit1332"

companyNames = []
companyArr = []
tickerArr = []
netWorth = []
dividend = []
volitility = []
tickerIndex = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]
netWorthIndex = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
dividendIndex = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39]
volatilityIndex= [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

shareBuy = 60

startTime = time.time()
# time, net worth, dividend, volitility

def runPrint(*commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print (rline.strip())
            rline = sfile.readline()
    except:
        print "Did not connect, exit"
        sock.close()
    finally:
        sock.close()
    
def run(*commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            return (rline.strip())
            rline = sfile.readline()
    except:
        print "Did not connect, exit"
        sock.close()
    finally:
        sock.close()
      
def currentCash():
    data = str(run("MY_CASH"))
    tempArr = []
    tempArr = str(data).split(" ")
    print float(tempArr[1])
    return float(tempArr[1])
      
def getTickers():
    data = str(run("SECURITIES"))
    tempArr = []
    tempArr = str(data).split(" ")
    for index in tickerIndex:
        tickerArr.append(tempArr[index])
        
        
def dataCollection():
    data = str(run("SECURITIES"))
    tempArr = []
    tempArr = str(data).split(" ")
    for index in netWorthIndex:
        netWorth.append(float(tempArr[index]))
    for index in dividendIndex:
        dividend.append(float(tempArr[index]))
    for index in volatilityIndex:
        volitility.append(float(tempArr[index]))

def getCompData(ticker):
    bidaskData = str(run("SECURITIES " + ticker))
    
def update(cm):
    bidaskData = str(run("ORDERS " + cm.name))
    tempArr = []
    tempArr = str(bidaskData).split(" ")
    for i in range(len(tempArr)):
        if (tempArr[i] == "ASK"):
            cm.currentAskPrice = float(tempArr[i + 2])
        if (tempArr[i] == "BID"):
            cm.currentBidPrice = float(tempArr[i + 2])
    print cm.currentBidPrice
    print cm.currentAskPrice

########### ALGO ##########

def createCompanyArray():
    getTickers()
    one = company(tickerArr[0])
    one.index = 0
    companyArr.append(one)
    
    two = company(tickerArr[1])
    two.index = 1
    companyArr.append(two)
    
    three = company(tickerArr[2])
    three.index = 2
    companyArr.append(three)
    
    four = company(tickerArr[3])
    four.index = 3
    companyArr.append(four)
    
    five = company(tickerArr[4])
    five.index = 4
    companyArr.append(five)
    
    six = company(tickerArr[5])
    six.index = 5
    companyArr.append(six)
    
    seven = company(tickerArr[6])
    seven.index = 6
    companyArr.append(seven)
    
    eight = company(tickerArr[7])
    eight.index = 7
    companyArr.append(eight)
    
    nine = company(tickerArr[8])
    nine.index = 8
    companyArr.append(nine)
    
    ten = company(tickerArr[9])
    ten.index = 9
    companyArr.append(ten)
    
    # for i in range(10):
        # ticker = tickerArr[i]
        # obj = company(ticker)
        # companyArr.append(obj)
        # companyArr[i].index = i
    
    
    # print companyArr[0].name
    # print companyArr[1].name
    # print companyArr[2].name
    # print companyArr[3].name
    # print companyArr[4].name
    # print companyArr[5].name
    # print companyArr[6].name
    # print companyArr[7].name
    # print companyArr[8].name
    # print companyArr[9].name
    
def trade():
    global shareBuy
    while True:
        for each in companyArr:
            update(each)
            print "---------------------------"
            print "Shares of " + each.name + " " + str(each.shares)
            print "Time of " + each.name + " " + str(each.time)
            print "Ask price of " + each.name + " " + str(each.currentAskPrice)
            print "Buy price of " + each.name + " " + str(each.currentBidPrice)
            print "---------------------------"
            runPrint("MY_ORDERS")
            print "---------------------------"
            runPrint("MY_SECURITIES")
            print "---------------------------"
            buy(each)
            sell(each)
        time.sleep(1)
        
def buy(cm):
    global shareBuy
    if (currentCash() - 600) > 0:
        shareBuy += 10
    if cm.shares == 0:
        cm.price = cm.currentBidPrice
            # TODO: write code...
        run("CLEAR_BID " + cm.name)
            # TODO: write code...
        run("BID " + cm.name + " " + str(cm.currentBidPrice*1.01)  + " " + str(shareBuy))
        print " ------------------ BID " + cm.name + " " + str(cm.currentBidPrice)  + " " + str(shareBuy)
        cm.shares += 1
        print "Buy " + cm.name
        runPrint("MY_CASH")
        
def sell(cm):
    global shareBuy
    if cm.shares == 1 and cm.currentAskPrice > (cm.price):
        run("CLEAR_ASK " + cm.name)
        run("ASK" + " " + cm.name + " " + str(cm.currentAskPrice * 0.996)  + " " + str(shareBuy))
        print " -------------- ASK" + " " + cm.name + " " + str(cm.currentAskPrice)  + " " + str(shareBuy)
        cm.shares -= 1
        print "Sell " + cm.name
        runPrint("MY_CASH")
        cm.reset()
        

    


# def 
    
    
        
# def updateData():
#     while (True):
#         mySecurityCollection(run("MY_SECURITIES"))
#         myOrderCollection(run("MY_ORDERS")) # my orders data
#         myCashCollection(run("MY_CASH")) # my cash data
#         marketSecurityCollection(run("SECURITIES")) # market Security
#         for x in tickerArr:
#             marketOrderCollection(run("ORDERS " + x)) # market Order
#         print ""
#         time.sleep(1)
    
# runPrint("BID NFLX 13 100")
# runPrint("MY_CASH")
# runPrint("MY_SECURITIES")


# dataCollection()
# getTickers()

# print tickerArr
# print netWorth
# print dividend
# print volitility

# currentCash()

# companyArr.append()

# plotData()


createCompanyArray()
# print companyArr[0].name
# print companyArr[1].name
# print companyArr[2].name
# for i in range(10):
#     print companyArr[i].name
# # runPrint("ORDERS YUM")
# yum = companyArr[9]
# update(yum)

trade()
# getTickers()
# runPrint("MY_ORDERS")
# runPrint("BID TSLA 160 1")
# runPrint("MY_CASH")
# runPrint("CLEAR_BID")
