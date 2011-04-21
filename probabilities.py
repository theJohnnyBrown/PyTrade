
from scipy.stats import norm
import utils
import numpy
from scipy import stats


def prob_between(value1, value2):
    #returns the area under the standard normal curve between value1 and value2
    #require value1<value2 and both values have been standardized

    area = norm.cdf(value2)-norm.cdf(value1);
    return area;

def prob_list(market_values, k):
    #generates a list of probabilities.  Choose large k for better accuracy

    numBars = k*2+1
    widthBar = 10.0*numpy.std(market_values)/numBars
    i = 0
    s = numpy.std(market_values)
    probs = []
    scores = []
    mean = numpy.mean(market_values)
    while i<numBars:
        low = mean-5*s+i*widthBar
        high = low+widthBar
        lowZ = (low-mean)/s
        highZ = (high-mean)/s
        area = prob_between(lowZ, highZ)
        probs.append(area)
        scores.append(low)
        i+=1
    scores.append(high)
    return probs, scores

def reg_line(market_trades, strategy_trades):
    #returns slope, intercept, r value, p value, and standard error of lists
    #can now find expected return on a strategy as a function of market price
    return stats.linregress(market_trades, strategy_trades)

def linear_expected_return(slope, intercept, value):
    return intercept+slope*value


def expected_return(market_trades, strategy_trades, market_values, k):
    slope1, intercept1, r_value1, p_value1, std_err1 = reg_line(market_trades, strategy_trades)
    prob_list1, markVals1 = prob_list(market_values, k)
    total = 0
    i = 0
    prob_list2 = []
    
    while i<=len(prob_list1):
        prob_list2.append(linear_expected_return(slope1, intercept1, markVals1[i]))
        i+=1

    i = 0
    mean1 = numpy.mean(strategy_trades)
    s1 = numpy.std(strategy_trades)
    probSum = 0


        
    while i<len(prob_list1):
        val1 = linear_expected_return(slope1, intercept1, (markVals1[i]+markVals1[i+1])/2)
        val2 = prob_list1[i]
        val3 = prob_between((prob_list2[i]-mean1)/s1,(prob_list2[i+1]-mean1)/s1)
        print(val1)
        print(val2)
        print(val3)
        print('')
        probSum = probSum+val2*val3
        total = total+val1*val2*val3
        i+=1

    if probSum == 0:
        print ('probSum is 0 and r val is')
        print (r_value1)
        print('')
        return mean1
    
    else:
        weight_factor = 1.0/probSum
        expected = r_value1*total*weight_factor + (1-r_value1)*mean1
        print(r_value1)
        print('')
        return expected
        
    
