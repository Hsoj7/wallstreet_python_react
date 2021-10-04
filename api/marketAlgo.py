from datetime import date
from datetime import timedelta
import pandas as pd
import yahoo_fin.stock_info as si
import yfinance as yf
import json

# All seeing algo
# -> VIX
# moving averages
# -> 10 year
# Take into account the various segments performance


# to do:
# take into account overnight reverse repurchase rate. This is the amount of money banks have
# -> Why kevin thinks the market won't dip right now. Looks into this at work
# include the high low index
# include CPI data?
# Figure out oil relation to stocks
# Figure out how the FED affects this. How what they say is important to the macro
# include the BPI, bullish percent index?
# FIX: if jsonMarketSegments keeps returning an error, put try catchs in each of the functions
# tax increase is bad for markets
# monetary policy, particularily M2. Look at monthly amounts. monthly % changes
# interest rates - loan rates. Look at historical data


class marketAlgo:
    def __init__(self):
        # Class variable so the API call only needs to be called once
        self.vix = 0
        self.tenYear = 0
        self.nasdaq = 0
        self.sp = 0
        self.dow = 0

    # Keep brainstorming what to do here
    # maybe return an overall seniment meter?
    # % chance the algo thinks its a bull market / bear market. Buy/sell on the macro level
    def marketAlgorithm(self):

        return 0

    # Figure out how to download the reverse repo data
    # Reverse Repurchase Agreements are the purchase of securities with the agreement
    # to sell them at a high price in the future.
    # When this is high, it means banks have way too much money and don't know what to do with it
    # This means the market might not fall very hard, too much money going in buying the dip
    def reverseRepoRate(self):

        return 0

    # Get montly CPI data
    # Find real versus expected data
    # Use this for the master algo
    def CPIData(self):

        return 0

    # Get current crude oil prices
    # Figure out what it's price means for the market
    # Use this for the master algo
    def oilData(self):

        return 0

    # Investopedia has a calculation for this
    # Maybe get this when doing the segments function because of less API calls
    def highLowIndex(self):

        return 0




# COMPLETED





    # Returns average daily % change based on the five stocks listed:
    # XOM, CVX, SU, EPD, NEE
    def energySegment(self):
        segmentDailyChange = 0

        # ExxonMobil
        XOM = si.get_quote_table("XOM")
        changeXOM = ((XOM['Quote Price'] / XOM['Previous Close']) - 1) * 100
        # Royal Dutch Shell
        CVX = si.get_quote_table("CVX")
        changeCVX = ((CVX['Quote Price'] / CVX['Previous Close']) - 1) * 100
        # Suncor Energy
        SU = si.get_quote_table("SU")
        changeSU = ((SU['Quote Price'] / SU['Previous Close']) - 1) * 100
        # NextEra Energy
        EPD = si.get_quote_table("EPD")
        changeEPD = ((EPD['Quote Price'] / EPD['Previous Close']) - 1) * 100
        # NextEra Energy
        NEE = si.get_quote_table("NEE")
        changeNEE = ((NEE['Quote Price'] / NEE['Previous Close']) - 1) * 100

        segmentDailyChange = (changeXOM + changeCVX + changeSU + changeEPD + changeNEE) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # CE, DD, FCX, NUE, CLF
    def materialsSegment(self):
        segmentDailyChange = 0

        # Celanese Corporation
        CE = si.get_quote_table("CE")
        changeCE = ((CE['Quote Price'] / CE['Previous Close']) - 1) * 100
        # DuPont - chemicals
        DD = si.get_quote_table("DD")
        changeDD = ((DD['Quote Price'] / DD['Previous Close']) - 1) * 100
        # Freeport - McMoRan
        FCX = si.get_quote_table("FCX")
        changeFCX = ((FCX['Quote Price'] / FCX['Previous Close']) - 1) * 100
        # Nucor - Steel production
        NUE = si.get_quote_table("NUE")
        changeNUE = ((NUE['Quote Price'] / NUE['Previous Close']) - 1) * 100
        # Cleveland-Cliffs - mining
        CLF = si.get_quote_table("CLF")
        changeCLF = ((CLF['Quote Price'] / CLF['Previous Close']) - 1) * 100

        segmentDailyChange = (changeCE + changeDD + changeFCX + changeNUE + changeCLF) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # ETN, LPX, SEB, BLDR, GNRC, CAT
    def industrialsSegment(self):
        segmentDailyChange = 0

        # Eaton corporation - Power mangement
        ETN = si.get_quote_table("ETN")
        changeETN = ((ETN['Quote Price'] / ETN['Previous Close']) - 1) * 100
        # Louisiana-Pacific corporation - materials manufacturer
        LPX = si.get_quote_table("LPX")
        changeLPX = ((LPX['Quote Price'] / LPX['Previous Close']) - 1) * 100
        # Seaboard Corporation - Conglomerate
        SEB = si.get_quote_table("SEB")
        changeSEB = ((SEB['Quote Price'] / SEB['Previous Close']) - 1) * 100
        # Builders First Source - Manufacturer
        BLDR = si.get_quote_table("BLDR")
        changeBLDR = ((BLDR['Quote Price'] / BLDR['Previous Close']) - 1) * 100
        # Caterpiller - Industrial Equipment
        CAT = si.get_quote_table("CAT")
        changeCAT = ((CAT['Quote Price'] / CAT['Previous Close']) - 1) * 100

        segmentDailyChange = (changeETN + changeLPX + changeSEB + changeBLDR + changeCAT) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # NRG, EXC, CNP, DUK, CATL
    def utilitiesSegment(self):
        segmentDailyChange = 0

        # NRG Energy - Nuclear
        NRG = si.get_quote_table("NRG")
        changeNRG = ((NRG['Quote Price'] / NRG['Previous Close']) - 1) * 100
        # Exelon - Nuclear
        EXC = si.get_quote_table("EXC")
        changeEXC = ((EXC['Quote Price'] / EXC['Previous Close']) - 1) * 100
        # Center Point Energy - Utilities Company
        CNP = si.get_quote_table("CNP")
        changeCNP = ((CNP['Quote Price'] / CNP['Previous Close']) - 1) * 100
        # Duke Energy - Holding company
        DUK = si.get_quote_table("DUK")
        changeDUK = ((DUK['Quote Price'] / DUK['Previous Close']) - 1) * 100
        # Southern Company - Gas and electric
        SO = si.get_quote_table("SO")
        changeSO = ((SO['Quote Price'] / SO['Previous Close']) - 1) * 100

        segmentDailyChange = (changeNRG + changeEXC + changeCNP + changeDUK + changeSO) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # REGN, MRNA, JNJ, UNH, CVS
    def healthcareSegment(self):
        segmentDailyChange = 0

        # Regernon pharmaceuticals - biotech
        REGN = si.get_quote_table("REGN")
        changeREGN = ((REGN['Quote Price'] / REGN['Previous Close']) - 1) * 100
        # Moderna - Bio tech
        MRNA = si.get_quote_table("MRNA")
        changeMRNA = ((MRNA['Quote Price'] / MRNA['Previous Close']) - 1) * 100
        # Johnson & Johnson - everything health care
        JNJ = si.get_quote_table("JNJ")
        changeJNJ = ((JNJ['Quote Price'] / JNJ['Previous Close']) - 1) * 100
        # United Health Group - Insurance
        UNH = si.get_quote_table("UNH")
        changeUNH = ((UNH['Quote Price'] / UNH['Previous Close']) - 1) * 100
        # CVS Health - Pharmacy company
        CVS = si.get_quote_table("CVS")
        changeCVS = ((CVS['Quote Price'] / CVS['Previous Close']) - 1) * 100

        segmentDailyChange = (changeREGN + changeMRNA + changeJNJ + changeUNH + changeCVS) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # SQ, V, JPM, WFC, AXP
    def financialsSegment(self):
        segmentDailyChange = 0

        # Square
        SQ = si.get_quote_table("SQ")
        changeSQ = ((SQ['Quote Price'] / SQ['Previous Close']) - 1) * 100
        # Visa
        V = si.get_quote_table("V")
        changeV = ((V['Quote Price'] / V['Previous Close']) - 1) * 100
        # JP Morgan
        JPM = si.get_quote_table("JPM")
        changeJPM = ((JPM['Quote Price'] / JPM['Previous Close']) - 1) * 100
        # Wells Fargo
        WFC = si.get_quote_table("WFC")
        changeWFC = ((WFC['Quote Price'] / WFC['Previous Close']) - 1) * 100
        # American Express
        AXP = si.get_quote_table("AXP")
        changeAXP = ((AXP['Quote Price'] / AXP['Previous Close']) - 1) * 100

        segmentDailyChange = (changeSQ + changeV + changeJPM + changeWFC + changeAXP) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # EBAY, WMT, HAS, TGT, SBUX
    def consumerDiscretionarySegment(self):
        segmentDailyChange = 0

        # EBAY
        EBAY = si.get_quote_table("EBAY")
        changeEBAY = ((EBAY['Quote Price'] / EBAY['Previous Close']) - 1) * 100
        # WalMart
        WMT = si.get_quote_table("WMT")
        changeWMT = ((WMT['Quote Price'] / WMT['Previous Close']) - 1) * 100
        # Hasbro
        HAS = si.get_quote_table("HAS")
        changeHAS = ((HAS['Quote Price'] / HAS['Previous Close']) - 1) * 100
        # Target
        TGT = si.get_quote_table("TGT")
        changeTGT = ((TGT['Quote Price'] / TGT['Previous Close']) - 1) * 100
        # StarBux
        SBUX = si.get_quote_table("SBUX")
        changeSBUX = ((SBUX['Quote Price'] / SBUX['Previous Close']) - 1) * 100

        segmentDailyChange = (changeEBAY + changeWMT + changeHAS + changeTGT + changeSBUX) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # TSN, PG, PEP, COST, KO
    def consumerStaplesSegment(self):
        segmentDailyChange = 0

        # Tyson Foods
        TSN = si.get_quote_table("TSN")
        changeTSN = ((TSN['Quote Price'] / TSN['Previous Close']) - 1) * 100
        # Protor and Gamble
        PG = si.get_quote_table("PG")
        changePG = ((PG['Quote Price'] / PG['Previous Close']) - 1) * 100
        # Pepsi
        PEP = si.get_quote_table("PEP")
        changePEP = ((PEP['Quote Price'] / PEP['Previous Close']) - 1) * 100
        # Costco
        COST = si.get_quote_table("COST")
        changeCOST = ((COST['Quote Price'] / COST['Previous Close']) - 1) * 100
        # Coke
        KO = si.get_quote_table("KO")
        changeKO = ((KO['Quote Price'] / KO['Previous Close']) - 1) * 100

        segmentDailyChange = (changeTSN + changePG + changePEP + changeCOST + changeKO) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # AAPL, TSLA, NVDA, AMD, AMAT, AMZN, MSFT
    def informationTechnologySegment(self):
        segmentDailyChange = 0

        # Apple
        AAPL = si.get_quote_table("AAPL")
        changeAAPL = ((AAPL['Quote Price'] / AAPL['Previous Close']) - 1) * 100
        # Tesla
        TSLA = si.get_quote_table("TSLA")
        changeTSLA = ((TSLA['Quote Price'] / TSLA['Previous Close']) - 1) * 100
        # Nvidia
        NVDA = si.get_quote_table("NVDA")
        changeNVDA = ((NVDA['Quote Price'] / NVDA['Previous Close']) - 1) * 100
        # AMD
        AMD = si.get_quote_table("AMD")
        changeAMD = ((AMD['Quote Price'] / AMD['Previous Close']) - 1) * 100
        # Applied Materials
        AMAT = si.get_quote_table("AMAT")
        changeAMAT = ((AMAT['Quote Price'] / AMAT['Previous Close']) - 1) * 100
        # Amazon
        AMZN = si.get_quote_table("AMZN")
        changeAMZN = ((AMZN['Quote Price'] / AMZN['Previous Close']) - 1) * 100
        # Microsoft
        MSFT = si.get_quote_table("MSFT")
        changeMSFT = ((MSFT['Quote Price'] / MSFT['Previous Close']) - 1) * 100

        segmentDailyChange = (changeAAPL + changeTSLA + changeNVDA + changeAMAT + changeAMZN + changeMSFT) / 6

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # VIAC, FOX, TMUS, FB, VZ
    def communicationServicesSegment(self):
        segmentDailyChange = 0

        # ViaCom CBS - Mass media
        VIAC = si.get_quote_table("VIAC")
        changeVIAC = ((VIAC['Quote Price'] / VIAC['Previous Close']) - 1) * 100
        # Fox network
        FOX = si.get_quote_table("FOX")
        changeFOX = ((FOX['Quote Price'] / FOX['Previous Close']) - 1) * 100
        # T Mobile - carrier
        TMUS = si.get_quote_table("TMUS")
        changeTMUS = ((TMUS['Quote Price'] / TMUS['Previous Close']) - 1) * 100
        # Facebook
        FB = si.get_quote_table("FB")
        changeFB = ((FB['Quote Price'] / FB['Previous Close']) - 1) * 100
        # Verizon - carrier
        VZ = si.get_quote_table("VZ")
        changeVZ = ((VZ['Quote Price'] / VZ['Previous Close']) - 1) * 100

        segmentDailyChange = (changeVIAC + changeFOX + changeTMUS + changeFB + changeVZ) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # NLY, AGNC, NRZ, SUI, WY
    def realEstateSegment(self):
        segmentDailyChange = 0

        # Annaly captial management
        NLY = si.get_quote_table("NLY")
        changeNLY = ((NLY['Quote Price'] / NLY['Previous Close']) - 1) * 100
        # AGNC investment corp - real estate investment trust company
        AGNC = si.get_quote_table("AGNC")
        changeAGNC = ((AGNC['Quote Price'] / AGNC['Previous Close']) - 1) * 100
        # New residential Investment
        NRZ = si.get_quote_table("NRZ")
        changeNRZ = ((NRZ['Quote Price'] / NRZ['Previous Close']) - 1) * 100
        # Sun Communities - Real Estate Investmnet trust company
        SUI = si.get_quote_table("SUI")
        changeSUI = ((SUI['Quote Price'] / SUI['Previous Close']) - 1) * 100
        # Weyerhaeuser - Real estate investment trust company
        WY = si.get_quote_table("WY")
        changeWY = ((WY['Quote Price'] / WY['Previous Close']) - 1) * 100

        segmentDailyChange = (changeNLY + changeAGNC + changeNRZ + changeSUI + changeWY) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # CCL, AMC, AAL, CMG, ABNB
    def recoverySegment(self):
        segmentDailyChange = 0

        # Carnival Cruise Line
        CCL = si.get_quote_table("CCL")
        changeCCL = ((CCL['Quote Price'] / CCL['Previous Close']) - 1) * 100
        # AMC theaters. I was thinking to not put this in bc its so volatile right now,
        # but I'll keep it for now
        AMC = si.get_quote_table("AMC")
        changeAMC = ((AMC['Quote Price'] / AMC['Previous Close']) - 1) * 100
        # American Airlines
        AAL = si.get_quote_table("AAL")
        changeAAL = ((AAL['Quote Price'] / AAL['Previous Close']) - 1) * 100
        # Chipotle mexiacn grill
        CMG = si.get_quote_table("CMG")
        changeCMG = ((CMG['Quote Price'] / CMG['Previous Close']) - 1) * 100
        # Air BNB
        ABNB = si.get_quote_table("ABNB")
        changeABNB = ((ABNB['Quote Price'] / ABNB['Previous Close']) - 1) * 100

        segmentDailyChange = (changeCCL + changeAMC + changeAAL + changeCMG + changeABNB) / 5

        return segmentDailyChange

    # Returns average daily % change based on the five stocks listed:
    # ZM, ROKU, ETSY, DPZ, AMZN
    def stayAtHomeSegment(self):
        segmentDailyChange = 0

        # Zoom
        ZM = si.get_quote_table("ZM")
        changeZM = ((ZM['Quote Price'] / ZM['Previous Close']) - 1) * 100
        # Roku
        ROKU = si.get_quote_table("ROKU")
        changeROKU = ((ROKU['Quote Price'] / ROKU['Previous Close']) - 1) * 100
        # Etsy
        ETSY = si.get_quote_table("ETSY")
        changeETSY = ((ETSY['Quote Price'] / ETSY['Previous Close']) - 1) * 100
        # Dominos Pizza
        DPZ = si.get_quote_table("DPZ")
        changeDPZ = ((DPZ['Quote Price'] / DPZ['Previous Close']) - 1) * 100
        # Amazon
        AMZN = si.get_quote_table("AMZN")
        changeAMZN = ((AMZN['Quote Price'] / AMZN['Previous Close']) - 1) * 100

        segmentDailyChange = (changeZM + changeROKU + changeETSY + changeDPZ + changeAMZN) / 5

        return segmentDailyChange

    # Calls the 11 market segment functions + recovery/stay at home. This takes ~1 minute to run.
    # Maybe create a data base at some point that contains this ran every few minutes
    # Need cloud server first for this
    def jsonMarketSegments(self):
        # print("Getting market segments")
        energySegment = self.energySegment()
        print("Returned energy")
        materialsSegment = self.materialsSegment()
        print("Returned materials")
        industrialsSegment = self.industrialsSegment()
        print("Returned industrials")
        utilitiesSegment = self.utilitiesSegment()
        print("Returned utilities")
        healthcareSegment = self.healthcareSegment()
        print("Returned healthcare")
        financialsSegment = self.financialsSegment()
        print("Returned financials")
        consumerDiscretionarySegment = self.consumerDiscretionarySegment()
        print("Returned consumer discretionaries")
        consumerStaplesSegment = self.consumerStaplesSegment()
        print("Returned consumer staples")
        informationTechnologySegment = self.informationTechnologySegment()
        print("Returned information technology")
        communicationServicesSegment = self.communicationServicesSegment()
        print("Returned communication services")
        realEstateSegment = self.realEstateSegment()
        print("Returned real estate")
        recoverySegment = self.recoverySegment()
        print("Returned recovery segment")
        stayAtHomeSegment = self.stayAtHomeSegment()
        print("Returned stay at home segment")

        # Create json obj of market segments
        segmentsJsonObj = {
        "Energy": energySegment,
        "Materials": materialsSegment,
        "Industrials": industrialsSegment,
        "Utilities": utilitiesSegment,
        "Healthcare": healthcareSegment,
        "Financials": financialsSegment,
        "Consumer Discretionaries": consumerDiscretionarySegment,
        "Consumer Staples": consumerStaplesSegment,
        "Information Technology": informationTechnologySegment,
        "Communication Services": communicationServicesSegment,
        "Real Estate": realEstateSegment,
        "Recovery": recoverySegment,
        "Stay at Home": stayAtHomeSegment
        }

        # Turn the json obj to string that front end parses
        jsonString = json.dumps(segmentsJsonObj)

        return jsonString



    # Returns the current quote for the DOW Jones index
    def getCurrentDOW(self):
        currentDOW = si.get_quote_table("^DJI")

        return currentDOW['Quote Price']

    # returns 50 day moving averge of DOW Jones index
    def fiftyDayDOW(self):
        if self.dow == 0:
            self.dow = yf.Ticker("^DJI")

        fiftyDayAverage = self.dow.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # returns 200 day moving averge of DOW Jones index
    def twoHundredDayDOW(self):
        if self.dow == 0:
            self.dow = yf.Ticker("^DJI")

        twoHundredDay = self.dow.history(period='200d')['Close']
        twoHundredDay = sum(twoHundredDay) / len(twoHundredDay)
        return twoHundredDay

    # Returns % difference between the 50/200 averages
    # This number should be positive
    # If it becomes negative, the market is falling off a cliff
    # The closer and closer it gets to 0, the more pain there will be
    def fiftyOverTwoHundDOW(self):
        fifty = self.fiftyDayDOW()
        twoHund = self.twoHundredDayDOW()

        difference = ((fifty / twoHund) - 1) * 100

        return difference



    # Returns the curren quote for the SP500 index
    def getCurrentSP(self):
        currentSP = si.get_quote_table("^GSPC")

        return currentSP['Quote Price']

    # returns 50 day moving averge of SP500
    def fiftyDaySP(self):
        if self.sp == 0:
            self.sp = yf.Ticker("^GSPC")

        fiftyDayAverage = self.sp.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # returns 200 day moving averge of SP500
    def twoHundredDaySP(self):
        if self.sp == 0:
            self.sp = yf.Ticker("^GSPC")

        twoHundredDay = self.sp.history(period='200d')['Close']
        twoHundredDay = sum(twoHundredDay) / len(twoHundredDay)
        return twoHundredDay

    # Returns % difference between the 50/200 averages
    # This number should be positive
    # If it becomes negative, the market is falling off a cliff
    # The closer and closer it gets to 0, the more pain there will be
    def fiftyOverTwoHundSP(self):
        fifty = self.fiftyDaySP()
        twoHund = self.twoHundredDaySP()

        difference = ((fifty / twoHund) - 1) * 100

        return difference



    # Returns the curren quote for the NASDAQ index
    def getCurrentNASDAQ(self):
        currentNASDAQ = si.get_quote_table("^IXIC")

        return currentNASDAQ['Quote Price']

    # returns 50 day moving averge of nasdaq
    def fiftyDayNASDAQ(self):
        if self.nasdaq == 0:
            self.nasdaq = yf.Ticker("^IXIC")

        fiftyDayAverage = self.nasdaq.history(period='50d')['Close']
        fiftyDayAverage = sum(fiftyDayAverage) / len(fiftyDayAverage)
        return fiftyDayAverage

    # returns 200 day moving averge of nasdaq
    def twoHundredDayNASDAQ(self):
        if self.nasdaq == 0:
            self.nasdaq = yf.Ticker("^IXIC")

        twoHundredDay = self.nasdaq.history(period='200d')['Close']
        twoHundredDay = sum(twoHundredDay) / len(twoHundredDay)
        return twoHundredDay

    # Returns % difference between the 50/200 averages
    # This number should be positive
    # If it becomes negative, the market is falling off a cliff
    # The closer and closer it gets to 0, the more pain there will be
    def fiftyOverTwoHundNASDAQ(self):
        fifty = self.fiftyDayNASDAQ()
        twoHund = self.twoHundredDayNASDAQ()

        difference = ((fifty / twoHund) - 1) * 100

        return difference



    # Returns the curren quote for the 10 year treasury
    def getTenYear(self):
        if self.tenYear == 0:
            self.tenYear = si.get_quote_table("^TNX")

        # print(self.tenYear)
        return self.tenYear['Quote Price']

    # Returns the daily change for the 10 year
    def getTenYearDailyChange(self):
        if self.tenYear == 0:
            self.tenYear = si.get_quote_table("^TNX")

        prevClose = self.tenYear['Previous Close']
        current = self.tenYear['Quote Price']

        change = (current / prevClose)

        # Determining if - percent of + percent
        if change < 1:
            change = (1 - change) * 100
            change = change * (-1)
        elif change > 1:
            change = (change - 1) * 100
        elif change == 1:
            change = 0

        # print("change = " + str(change))
        return change

    # Returns the percentile based on the last 5 years of where the 10year is sitting
    def tenYearPercentile(self):
        tenYearPercentile = 0

        currentPrice = self.getTenYear()

        try:
            if currentPrice > 3.1:
                tenYearPercentile = 100
            elif currentPrice > 2.9:
                tenYearPercentile = 95
            elif currentPrice > 2.7:
                tenYearPercentile = 90
            elif currentPrice > 2.5:
                tenYearPercentile = 85
            elif currentPrice > 2.4:
                tenYearPercentile = 80
            elif currentPrice > 2.3:
                tenYearPercentile = 75
            elif currentPrice > 2.2:
                tenYearPercentile = 70
            elif currentPrice > 2.1:
                tenYearPercentile = 65
            elif currentPrice > 2.0:
                tenYearPercentile = 60
            elif currentPrice > 1.9:
                tenYearPercentile = 55
            elif currentPrice > 1.8:
                tenYearPercentile = 50
            elif currentPrice > 1.7:
                tenYearPercentile = 45
            elif currentPrice > 1.6:
                tenYearPercentile = 40
            elif currentPrice > 1.5:
                tenYearPercentile = 35
            elif currentPrice > 1.4:
                tenYearPercentile = 30
            elif currentPrice > 1.3:
                tenYearPercentile = 25
            elif currentPrice > 1.2:
                tenYearPercentile = 20
            elif currentPrice > 1.1:
                tenYearPercentile = 15
            elif currentPrice > 0.9:
                tenYearPercentile = 10
            else:
                tenYearPercentile = 5
        except:
            print("tenYearPercentile error")

        return tenYearPercentile



    # Returns the current (or close if after hours) quote of the CBOE volatility index ^VIX
    def getVIX(self):
        if self.vix == 0:
            # This returns a JSON object of all the info needed about the VIX
            self.vix = si.get_quote_table("^VIX")

        return self.vix['Quote Price']

    # Returns the percent daily change of the VIX
    def getVIXDailyChange(self):
        if self.vix == 0:
            self.vix = si.get_quote_table("^VIX")

        prevClose = self.vix['Previous Close']
        current = self.vix['Quote Price']

        change = (current / prevClose)

        # If the VIX is down, make sure the percent is negative
        # If the VIX is up, make sure the percent is positive
        # Else, it just happens to be 0, return 0
        if change < 1:
            change = (1 - change) * 100
            change = change * (-1)
        elif change > 1:
            change = (change - 1) * 100
        elif change == 1:
            change = 0

        # print("change = " + str(change))
        return change

    # Returns the percentile of panic on the given day
    # 0-30% is fairly low
    # 30%-50% is moderate
    # Above 50% is getting high
    # Above 80% is pure panic
    def VIXPanicPercentile(self):
        panicPercent = 0

        if self.vix == 0:
            self.vix = si.get_quote_table("^VIX")

        current = self.vix['Quote Price']
        # print("current = " + str(current))

        try:
            if current > 50:
                panicPercent = 100
            elif current > 47:
                panicPercent = 95
            elif current > 44:
                panicPercent = 90
            elif current > 41:
                panicPercent = 85
            elif current > 38:
                panicPercent = 80
            elif current > 36:
                panicPercent = 75
            elif current > 34:
                panicPercent = 70
            elif current > 32:
                panicPercent = 65
            elif current > 30:
                panicPercent = 60
            elif current > 28:
                panicPercent = 55
            elif current > 26:
                panicPercent = 50
            elif current > 24:
                panicPercent = 45
            elif current > 22:
                panicPercent = 40
            elif current > 20:
                panicPercent = 35
            elif current > 18:
                panicPercent = 30
            elif current > 16:
                panicPercent = 25
            elif current > 14:
                panicPercent = 20
            elif current > 12.5:
                panicPercent = 15
            elif current > 11:
                panicPercent = 10
            else:
                panicPercent = 5
        except:
            print("panicPercent error")

        return panicPercent



if __name__ == '__main__':
    algo = marketAlgo()

    # energy = algo.energySegment()
    # print("/energySegment returned: " + str(energy))
    # print("")
    # materials = algo.materialsSegment()
    # print("/materialsSegment returned: " + str(materials))
    # print("")
    # industrials = algo.industrialsSegment()
    # print("/industrialsSegment returned: " + str(industrials))
    # print("")
    # utilities = algo.utilitiesSegment()
    # print("/utilitiesSegment returned: " + str(utilities))
    # print("")
    # healthCare = algo.healthcareSegment()
    # print("/healthcareSegment returned: " + str(healthCare))
    # print("")
    # financials = algo.financialsSegment()
    # print("/financialsSegment returned: " + str(financials))
    # print("")
    # consumerDiscretionary = algo.consumerDiscretionarySegment()
    # print("/consumerDiscretionarySegment returned: " + str(consumerDiscretionary))
    # print("")
    # consumerStaples = algo.consumerStaplesSegment()
    # print("/consumerStaplesSegment returned: " + str(consumerStaples))
    # print("")
    # informationTechnology = algo.informationTechnologySegment()
    # print("/informationTechnologySegment returned: " + str(informationTechnology))
    # print("")
    # communicationServices = algo.communicationServicesSegment()
    # print("/communicationServicesSegment returned: " + str(communicationServices))
    # print("")
    # realEstate = algo.realEstateSegment()
    # print("/realEstateSegment returned: " + str(realEstate))
    # print("")
    # recovery = algo.recoverySegment()
    # print("/recoverySegment returned: " + str(recovery))
    # print("")
    # stayAtHome = algo.stayAtHomeSegment()
    # print("/stayAtHomeSegment returned: " + str(stayAtHome))
    # print("")
    jsonSegments = algo.jsonMarketSegments()
    print("/jsonMarketSegments returned: ")
    print(jsonSegments)
    print("")



    # print("Testing getCurrentDOW():")
    # currentDOW = algo.getCurrentDOW()
    # print("/getCurrentDOW returned: " + str(currentDOW))
    # print("")

    # print("Testing fiftyDayDOW():")
    # fiftyDOW = algo.fiftyDayDOW()
    # print("/fiftyDayDOW returned: " + str(fiftyDOW))
    # print("")

    # print("Testing twoHundredDayDOW():")
    # twoHundredDOW = algo.twoHundredDayDOW()
    # print("/twoHundredDayDOW returned: " + str(twoHundredDOW))
    # print("")

    # print("Testing fiftyOverTwoHundDOW():")
    # fiftyOverTwoHundDOW = algo.fiftyOverTwoHundDOW()
    # fiftyOverTwoHundDOW = "{:.4f}".format(fiftyOverTwoHundDOW)
    # print("/fiftyOverTwoHundDOW returned: " + str(fiftyOverTwoHundDOW))
    # print("")


    # print("Testing getCurrentSP():")
    # currentSP = algo.getCurrentSP()
    # print("/getCurrentSP returned: " + str(currentSP))
    # print("")

    # print("Testing fiftyDaySP():")
    # fiftySP = algo.fiftyDaySP()
    # print("/fiftyDaySP returned: " + str(fiftySP))
    # print("")

    # print("Testing twoHundredDaySP():")
    # twoHundredSP = algo.twoHundredDaySP()
    # print("/twoHundredDaySP returned: " + str(twoHundredSP))
    # print("")

    # print("Testing fiftyOverTwoHundSP():")
    # fiftyOverTwoHundSP = algo.fiftyOverTwoHundSP()
    # fiftyOverTwoHundSP = "{:.4f}".format(fiftyOverTwoHundSP)
    # print("/fiftyOverTwoHundSP returned: " + str(fiftyOverTwoHundSP))
    # print("")



    # print("Testing getCurrentNASDAQ():")
    # currentNas = algo.getCurrentNASDAQ()
    # print("/getCurrentNASDAQ returned: " + str(currentNas))
    # print("")

    # print("Testing fiftyDayNASDAQ():")
    # fiftyNas = algo.fiftyDayNASDAQ()
    # print("/fiftyDayNASDAQ returned: " + str(fiftyNas))
    # print("")

    # print("Testing twoHundredDayNASDAQ():")
    # twoHundredNas = algo.twoHundredDayNASDAQ()
    # print("/twoHundredDayNASDAQ returned: " + str(twoHundredNas))
    # print("")

    # print("Testing fiftyOverTwoHundNASDAQ():")
    # fiftyOverTwoHundNas = algo.fiftyOverTwoHundNASDAQ()
    # fiftyOverTwoHundNas = "{:.4f}".format(fiftyOverTwoHundNas)
    # print("/fiftyOverTwoHundNASDAQ returned: " + str(fiftyOverTwoHundNas))
    # print("")



    # print("Testing getTenYear():")
    # tenYear = algo.getTenYear()
    # print("/getTenYear returned: " + str(tenYear))
    # print("")

    # print("Testing getTenYearDailyChange():")
    # tenYearChange = algo.getTenYearDailyChange()
    # print("/getTenYearDailyChange returned: " + str(tenYearChange))
    # print("")

    # print("Testing tenYearPercentile():")
    # tenYearPercentile = algo.tenYearPercentile()
    # print("/tenYearPercentile returned: " + str(tenYearPercentile))
    # print("")



    # print("Testing getVIX():")
    # vix = algo.getVIX()
    # print("/getVIX returned: " + str(vix))
    # print("")

    # print("Testing getVIXDailyChange():")
    # vixChange = algo.getVIXDailyChange()
    # vixChange = "{:.2f}".format(vixChange)
    # print("/getVIXDailyChange returned: " + str(vixChange) + "%")
    # print("")

    # print("Testing VIXPanicPercentile():")
    # vixPanic = algo.VIXPanicPercentile()
    # print("/VIXPanicPercentile returned: " + str(vixPanic))
    # print("")
