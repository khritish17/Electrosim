'''
    API of Electromulation
'''

from components import resistors as restr

def resistors(resistance, input_, power_rating = 0.125, current_channel = False):
    RESISTOR = restr.Resistors(resistance, input_, power_rating, current_channel)
    voltage, current = RESISTOR.resistor_output()
    return voltage, current