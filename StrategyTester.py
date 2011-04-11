from pylab import *
import utils

class StrategyTester:

    def __init__(self, capital):
        self.capital = capital

    def apply(self, strategy, pricepoints):
        print "starting capital: %d" % self.capital
        decisions = strategy(pricepoints)
        last = 0
        for i,decision in enumerate(decisions):
            self.capital = self.capital - decision*pricepoints[i]
            if (decision != 0): last = decision
            if (decision > 0):
                print "buy:  %d shares at $%d" % (decision, pricepoints[i])
            elif (decision < 0):
                print "sell: %d shares at $%d" % (-1*decision, pricepoints[i])
            print "remaining capital: %d at time=%d" % (self.capital, i)
        if (last > 0): self.capital = self.capital + last*pricepoints[len(pricepoints)-1]
        print "final capital: %d over %d data points" % (self.capital, len(pricepoints))
        
def plot_strat(decisions, pricepoints, filename):
    assert (len(decisions) == len(pricepoints))
    plot(pricepoints)
    for i, decision in enumerate(decisions):
        if(decision > 0):
            plot(i,pricepoints[i],'^')
        elif(decision < 0):
            plot(i,pricepoints[i],'v')

    plot(utils.EMA_list(pricepoints,15))
    plot(utils.SMA_list(pricepoints, 15))
    savefig(filename)
        
