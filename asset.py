import sources
import collections
import datetime

class Asset:

    def __init__(self, ticker):
        self.data = None
        for mod in sources.SOURCES:
            src = __import__('sources.'+mod)
            if(src.has_data(ticker)):
                self.data = src.get_data(ticker)
        if(self.data):
            self.quotes = [Quote(d) for d in data]




class Quote:
    
    def __init__(self, qt_info):
        if isinstance(qt_info, str):
            row = qt_info.split(',')
            when = [int(el) for el in row[0].strip().split('-') ]
            self.date = datetime.date(*when)
            self.open = float(row[1])
            self.high = float(row[2])
            self.low = float(row[3])
            self.close = float(row[4])
            self.volume = float(row[5])
            self.adj_close = float(row[6])
            
        if isinstance(qt_info, collection.Iterable):
            pass
        if isinstance(qt_info, Quote):
            pass
            
            
        


