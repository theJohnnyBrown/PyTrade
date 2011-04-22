import datetime
import collections
from itertools import *

def get_column(filename, col, skip=0):
    f = open(filename)
    for i in range(0,skip):
        f.readline()
    return map(lambda l: l.split(',')[col],f.readlines())

def EMA_list(values, length):
    slices = k_wise(length, values)
    return ([0]*(length-1))+map(lambda s: EMA_for_point(s, length), slices)

def EMA_for_point(values, length):
    assert (length <= len(values)) 
    x_0 = float(-1)/(1-2**length)
    i = len(values)-length
    result = 0
    for i, el in enumerate(take_r(length, values)):
        result = result+el*(2**i)*x_0
    return result

#exp = map(lambda x: ema.EMA_for_point(closes[:x],15), range(0,len(closes)))

def SMA_for_point(values, length):
    if(length > len(values)):
        return mean(values)
    else:
        return mean(take_r(length, values))

def SMA_list(values, length):
    slices = k_wise(length, values)
    return ([0]*(length-1))+map(mean, slices)

def mean(numbers):
    if(len(numbers) == 0):
        return 0
    else:
        return reduce(lambda x,y: x+y, numbers)/float(len(numbers))

def take_r(n,l):
    if(l.__class__ == collections.deque):
        result = collections.deque()
        for i in range(0, n):
            result.appendleft(l[len(l)-1])
            l.rotate(1)
        l.rotate(n)
    else:
        result =  l[len(l)-n:]
    return result

def leave_r(n,l):
    if(l.__class__ == collections.deque):
        result = collections.deque()
        l.rotate(n)
        for i in range(0, len(l)-n):
            result.appendleft(l[len(l)-1])
            l.rotate(1)
    else:
        result =  l[:len(l)-n]

    return result

def roi(i_f):
    """gives the return on investment from i_f[0] to i_f[1] (difference divided by initial investment, or percent change between the two values) """
    return (i_f[1]-float(i_f[0]))/i_f[0]

    return (i_f[1]-float(i_f[0]))/i_f[0]

def roistar(*args):
    return (args[1]-float(args[0]))/args[0]

def rois(points):
    return map(roi, pairwise(points))


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def pairwise(iterable):
     "s -> (s0,s1), (s1,s2), (s2, s3), ..."
     a, b = tee(iterable)
     next(b, None)
     return izip(a, b)

def k_wise(k, iterable):
    "s -> [(s0,s1,...sk), (s1,s2,...s[k+1]), (s2,s3,...s[k+2])] .... \n length of result is len(iterable)-k+1, as incomplete k-tuples at the end are left out"
    iterators = tee(iterable, k)
    for i in range(k):
        consume(iterators[i],i)
    return izip(*iterators)


def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def date_from(datestring):
    when = [int(el) for el in datestring.strip().split('-') ]
    return datetime.date(*when)
