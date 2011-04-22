import urllib

def yahoo_url(start, end, ticker):
    base_url = 'http://ichart.finance.yahoo.com/table.csv?s=%s&d=%s&e=%s&f=%s&g=%s&a=%s&b=%s&c=%s&ignore=.csv'
    return base_url % (ticker, str(end.month-1), str(end.day), str(end.year),'d', str(start.month-1), str(start.day), str(start.year))
# >>> fd = urllib.open('http://ichart.finance.yahoo.com/table.csv?s=F&d=3&e=22&f=2011&
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'open'
# >>> fd = urllib.urlopen('http://ichart.finance.yahoo.com/table.csv?s=F&d=3&e=22&f=2011&g=d&a=0&b=3&c=1977&ignore=.csv')

# 'http://ichart.finance.yahoo.com/table.csv?s=F&d=3&e=22&f=2011&g=d&a=0&b=3&c=1977&ignore=
# 'http://ichart.finance.yahoo.com/table.csv?s=%s&d=%s&e=%s&f=%s&g=%s&a=%s&b=%s&c=%s&ignore=
