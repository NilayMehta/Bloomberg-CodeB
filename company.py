class company(object):
    name = ""
    shares = 0
    price = 0
    total_investment = 0
    dividend = 0
    volatility = 0
    index = -1
    currentAskPrice = 0
    currentBidPrice = 0
    time = 0

    tickerIndex = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]
    tempArr = []

    
    def __init__(self, ticker):
        self.name = str(ticker)
        # data = str(run("SECURITIES"))
        # tempArr = str(data).split(" ")
        # for index in tickerIndex:
        #     tickerArr.append(tempArr[index])
        # for i in range(10):
        #     if ticker.equauls(tickerArr[i]):
        #         self.index = i


    def company(sh, div, vol, pr):
        # global shares
        # global total_investment
        # global dividend
        # global volatility
        # global price
        self.shares = sh
        self.dividend = div
        self.volatility = vol
        self.price = pr
        self.total_investment = price * shares
        

    # def update():
    #     global shares
    #     global total_investment
    #     global dividend
    #     global volatility
        
    #     for index in netWorthIndex:
    #         netWorth.append(float(tempArr[index]))
    #     for index in dividendIndex:
    #         dividend.append(float(tempArr[index]))
    #     for index in volatilityIndex:
    #         volitility.append(float(tempArr[index]))
        
        
    def reset(self):
        self.shares = 0
        self.price = 0
        self.total_investment = 0
        self.dividend = 0
        self.volatility = 0
        self.time = 0
            
    # def getBoughtPrice(self):
    #     global price
    #     return price
        
    # def setBoughtPrice(self, input):
    #     global price
    #     price = input
        
    # def getName(self):
    #     global name
    #     return name
        
    # def setName(self, input):
    #     global name
    #     name = input
        
    # def getCurrentAskPrice():
    #     global currentAskPrice
    #     return currentAskPrice
        
    # def setCurrentAskPrice(input):
    #     global currentAskPrice
    #     currentAskPrice = input
        
    # def getCurrentBidPrice():
    #     global currentBidPrice
    #     return currentBidPrice
        
    # def setCurrentBidPrice(input):
    #     global currentBidPrice
    #     currentBidPrice = input
