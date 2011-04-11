from utils import EMA_list as emas
from utils import SMA_list as smas
import collections
import itertools

def ema_sma(buy_amt, sell_amt, length):
    def ema_v_sma(points):
        """simply buys if EMA overtakes SMA, and sells if it falls below"""
        decisions = collections.deque()
        last = 0
        pts = itertools.izip(points, smas(points,length), emas(points,length))
        for i, day in enumerate(pts):
            p, sma, ema = day
            if(ema>sma and last <= 0):#buy TODO should not buy on first non-zero
                decisions.append(buy_amt)
                last = 1
            elif(ema<sma and last > 0):
                decisions.append(-sell_amt)
                last = -1
            else: decisions.append(0)
        return decisions
    return ema_v_sma


