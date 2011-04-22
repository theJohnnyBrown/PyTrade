from collections import deque
import PyTrade.constants as c
import PyTrade.utils as utils
import os
from PyTrade.asset import Quote

def has_data(ticker, start, end):
    """ returns whether this data source has data available for the specified asset and date range """
    #import pdb; pdb.set_trace()
    try:
        f = open(os.path.join(c.data_dir,ticker+'.csv'))
        utils.consume(f,1)
        last = utils.date_from(f.next().split(',')[0])
        f.seek(-100,os.SEEK_END)
        tail = f.read().splitlines()
        first = utils.date_from(tail[len(tail)-1].split(',')[0])
        
        return (first <= start and last >= end)
    except IOError:
        return False

def get_data(ticker, start, end):
    """Returns price data for the given ticker between the given dates as a list of Quotes"""
    if not has_data(ticker, start, end):
        return None
    else:
        csv = open(os.path.join(c.data_dir, ticker+'.csv'))
        csv.next()
        lines = deque()
        for line in csv:
            d=utils.date_from(line.split(',')[0])
            if(d >= start and d <= end):
                lines.append(line)

        return lines
