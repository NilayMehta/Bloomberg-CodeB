import socket
import sys
import csv
import time
import numpy
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

user = "algorhythms"
password = "nit1332"

tickerArr = ["AMZN", "DIS", "FB", "GOOGL", "IBM", "IVN", "KING", "KO", "NFLX", "TSLA"]
tickerIndex = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]

startTime = time.time()
# time, net worth, dividend, volitility
AMZN = [[], [], [], []]
DIS = [[], [], [], []]
FB = [[], [], [], []]
GOOGL = [[], [], [], []]
IBM = [[], [], [], []]
IVW = [[], [], [], []]
KING = [[], [], [], []]
KO = [[], [], [], []]
NFLX = [[], [], [], []]
TSLA = [[], [], [], []]

#arrays to CSV
# command : numpy.asarray([1,2,3], [4,5,6], [7,8,9])
# save text : numpy.savetxt("AMZN.csv", data to be saved, ",")

# numpy.savetxt("SecuritiesCollection.csv", securityCollectionData, ",")
# numpy.savetxt("OrdersCollectionData.csv", ordersCollectionData, ",")
# numpy.savetxt("CashCollectionData.csv", cashCollectionData, ",")
# numpy.savetxt("MarketOrderCollection.csv", marketOrderCollection, ",")
# numpy.savetxt("SecuritiesCollection.csv", securityCollectionData, ",")

def toCSV():
    
    x = 0
    for cacheTime in time:
        saveLine = securityCollectionData + ", " + cashCollectionData + ", " + marketOrderCollection + ", " + securityCollectionData
        saveFile = open("Data.csv", "a")
          saveFile.write(saveLine)
          saveFile.close();
          x+=1
        




    
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

def subscribe():
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\nSUBSCRIBE\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    except:
        print "Did not connect, exit"
        sock.close()
    finally:
        sock.close()
      
def dataCollection(input):
    data = input
    tempArr = []
    tempArr = str(data).split(" ")
    # AMZN
    AMZN[0].append(time.time() - startTime)
    AMZN[1].append(tempArr[tickerIndex[0] + 1])
    AMZN[2].append(tempArr[tickerIndex[0] + 2])
    AMZN[3].append(tempArr[tickerIndex[0] + 3])
    print "AMZN"
    print AMZN
    # DIS
    DIS[0].append(time.time() - startTime)
    DIS[1].append(tempArr[tickerIndex[1] + 1])
    DIS[2].append(tempArr[tickerIndex[1] + 2])
    DIS[3].append(tempArr[tickerIndex[1] + 3])
    print "DIS"
    print DIS
    # FB
    FB[0].append(time.time() - startTime)
    FB[1].append(tempArr[tickerIndex[2] + 1])
    FB[2].append(tempArr[tickerIndex[2] + 2])
    FB[3].append(tempArr[tickerIndex[2] + 3])
    print "FB"
    print FB
    # GOOGL
    GOOGL[0].append(time.time() - startTime)
    GOOGL[1].append(tempArr[tickerIndex[3] + 1])
    GOOGL[2].append(tempArr[tickerIndex[3] + 2])
    GOOGL[3].append(tempArr[tickerIndex[3] + 3])
    print "GOOGL"
    print GOOGL
    # IBM
    IBM[0].append(time.time() - startTime)
    IBM[1].append(tempArr[tickerIndex[4] + 1])
    IBM[2].append(tempArr[tickerIndex[4] + 2])
    IBM[3].append(tempArr[tickerIndex[4] + 3])
    print "IBM"
    print IBM
    # IVN
    IVN[0].append(time.time() - startTime)
    IVN[1].append(tempArr[tickerIndex[5] + 1])
    IVN[2].append(tempArr[tickerIndex[5] + 2])
    IVN[3].append(tempArr[tickerIndex[5] + 3])
    print "IVN"
    print IVN
    # KING
    KING[0].append(time.time() - startTime)
    KING[1].append(tempArr[tickerIndex[6] + 1])
    KING[2].append(tempArr[tickerIndex[6] + 2])
    KING[3].append(tempArr[tickerIndex[6] + 3])
    print "KING"
    print KING
    # KO
    KO[0].append(time.time() - startTime)
    KO[1].append(tempArr[tickerIndex[7] + 1])
    KO[2].append(tempArr[tickerIndex[7] + 2])
    KO[3].append(tempArr[tickerIndex[7] + 3])
    print "KO"
    print KO
    # NFLX
    NFLX[0].append(time.time() - startTime)
    NFLX[1].append(tempArr[tickerIndex[8] + 1])
    NFLX[2].append(tempArr[tickerIndex[8] + 2])
    NFLX[3].append(tempArr[tickerIndex[8] + 3])
    print "NFLX"
    print NFLX
    # TSLA
    TSLA[0].append(time.time() - startTime)
    TSLA[1].append(tempArr[tickerIndex[9] + 1])
    TSLA[2].append(tempArr[tickerIndex[9] + 2])
    TSLA[3].append(tempArr[tickerIndex[9] + 3])
    print "TSLA"
    print TSLA
    
def mySecurityCollection(input) : # my securities data
    securityCollectionData = input 
    
def myOrderCollection(input) : # my orders data
    ordersCollectionData = input
    
def myCashCollection(input) : # my cash data
    cashCollectionData = input
    
def marketSecurityCollection(input) : # market Security
    marketSecurityCollection = input
    
def marketOrderCollection(input) : # market Order
    marketOrderCollection = input
    
def execute():
    while (True):
        mySecurityCollection(run("MY_SECURITIES"))
        
        myOrderCollection(run("MY_ORDERS")) # my orders data
        
        myCashCollection(run("MY_CASH")) # my cash data
        
        marketSecurityCollection(run("SECURITIES")) # market Security
        
        for x in tickerArr:
            marketOrderCollection(run("ORDERS " + x)) # market Order
        
        print ""
        time.sleep(1)
        
def plotData():
    plt.ion() ## Note this correction
    fig=plt.figure()
    plt.axis([0,1000,0,1])
    
    i=0
    x=list()
    y=list()
    
    while i <1000:
        temp_y=np.random.random();
        x.append(i);
        y.append(temp_y);
        plt.scatter(i,temp_y);
        i+=1;
        plt.show()
        plt.pause(0.0001) #Note this correction
    
# Run program    
    execute()

# data = str(run("SECURITIES"))
# dataCollection(data)

# plotData()