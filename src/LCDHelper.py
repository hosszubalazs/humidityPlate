import src.constants as c

def map_heat_to_bgcolor(tempr):
    if tempr < 18:
        return c.LCD_COLD_BLUE
    elif tempr > 23:
        return c.LCD_HOT_RED
    else:
        return c.LCD_NICE_GREEN
