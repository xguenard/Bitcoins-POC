import sys
from PySide import QtGui
import requests
import json
import bitcoin
import threading
import time

class ApiCaller(threading.Thread):
    def __init__(self , ui_manager):
        threading.Thread.__init__(self)
        self.ui_manager = ui_manager
        self.kraken = []
        self.coinbase = []
        self.btc_e = []

    def FillKraken(self):
        self.kraken = []
        try:
            r = requests.post('https://api.kraken.com/0/public/Ticker'
                    ,data=json.dumps({"pair":"XXBTZUSD"})
                    ,headers={"content-type":"application/json"})
            self.kraken.append( r.json()['result']['XXBTZUSD']['c'][0])
        except:
            self.kraken.append(-1)
        
        try:
            r = requests.post('https://api.kraken.com/0/public/Ticker'
                    ,data=json.dumps({"pair":"XXBTZEUR"})
                    ,headers={"content-type":"application/json"})
            self.kraken.append( r.json()['result']['XXBTZEUR']['c'][0])
        except:
            self.kraken.append(-1)


    def FillCoinbase(self):
        self.coinbase = []
        try:
            r = requests.get('https://api.exchange.coinbase.com/products/BTC-USD/ticker') 
            self.coinbase.append( r.json()['price'])
        except:
            self.coinbase.append(-1)

        try:
            r = requests.get('https://api.exchange.coinbase.com/products/BTC-EUR/ticker') 
            self.coinbase.append( r.json()['price'])
        except:
            self.coinbase.append(-1)

    def FillBtc_e(self):
       self.btc_e = []
       try:
           r = requests.get('https://btc-e.com/api/2/btc_usd/ticker') 
           self.btc_e.append( r.json()['ticker']['last'])
       except:
           self.btc_e.append(-1)
       try:
           r = requests.get('https://btc-e.com/api/2/btc_eur/ticker') 
           self.btc_e.append( r.json()['ticker']['last'])
       except:
           self.btc_e.append(-1)
    def run(self):
        while 1:
            self.FillKraken()
            self.FillCoinbase()
            self.FillBtc_e()
            print( self.kraken )
            print( self.coinbase )
            print( self.btc_e)
            self.Update_UI()
            time.sleep( 5 )

    def Update_UI(self):
        self.ui_manager.data[0].setText( str( self.kraken[0] ))
        self.ui_manager.data[1].setText( str( self.kraken[1] ))

        self.ui_manager.data[2].setText( str( self.coinbase[0] ))
        self.ui_manager.data[3].setText( str( self.coinbase[1] ))

        self.ui_manager.data[4].setText( str( self.btc_e[0] ))
        self.ui_manager.data[5].setText( str( self.btc_e[1] ))

class GuiManager(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Bitcoin Exchanges")
        self.setGeometry(200 , 200 , 400 , 400 )

        grid = QtGui.QGridLayout()
        exchanges = [ "Kraken" , "Coinbase" , "Btc-e" ]
        pairs = [ "BTC-EUR" , "BTC-USD"]
        
        self.data = []
        ii = 0
        for i in exchanges :
            grid.addWidget( QtGui.QLabel( i  + " : ") , ii , 0 )
            self.data.append( QtGui.QLabel( str( 0.0 ) ))
            self.data.append( QtGui.QLabel( str( 0.0 ) ))
            kk = 1
            for k in pairs :
                grid.addWidget(QtGui.QLabel( k ) , ii , kk )
                grid.addWidget(self.data[ ii*2 + kk//2 ] , ii , kk + 1 )
                kk += 2
            ii += 1

        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(grid)
        self.setCentralWidget(centralWidget)
        self.show()

        

def main():
    app = QtGui.QApplication(sys.argv)
    test = GuiManager()
    api_caller = ApiCaller(test)
    api_caller.start()
    app.exec_()
    api_caller.join()
    sys.exit()

if __name__ == "__main__":
    main()
