def parse_temp(value):
    return parse_with_unit(value,"*C")

def parse_humidity(value):
    return parse_with_unit(value,"*%")

def parse_with_unit(value, unit):
    return '{0:0.1f}'.format(value)+unit
