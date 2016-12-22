def parseTemp(value):
    return parseWithUnit(value,"*C")

def parseHumidity(value):
    return parseWithUnit(value,"*%")

def parseWithUnit(value, unit):
    return '{0:0.1f}'.format(value)+unit
