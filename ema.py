

def EMA_for_point(values, length):
    if(len(values) == 1 or length == 1):
        return values[0]
    elif(len(values) == 0):
        return 0
    else:
        alpha, n  = float(2)/(length+1), len(values)
        return alpha*values[n-1]+(1-alpha)*(EMA_for_point(values[:n-1], length-1))

#exp = map(lambda x: ema.EMA_for_point(closes[:x],15), range(0,len(closes)))

def SMA_for_point(values, length):
    if(length > len(values)):
        return mean(values)
    else:
        return mean(values[len(values)-length:])

def mean(numbers):
    if(len(numbers) == 0):
        return 0
    else:
        return reduce(lambda x,y: x+y, numbers)/float(len(numbers))
