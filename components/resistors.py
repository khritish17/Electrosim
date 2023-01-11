'''
    All the units are in SI unit.
    Power rating in Watt
    Resistance in Ohm
    voltage in Volts
    Current in Amps

    voltage is the Potential difference across the resistor

    Specs:
    
'''
import numpy as np

class Resistors:
    def __init__(self, resistance, input_ , power_rating = 0.125, current_channel = False) -> None:
        self.resistance = resistance
        self.input_ = input_
        self.current_channel = current_channel
        self.power_rating = power_rating
        self.voltage = None
        self.current = None
        self.channel_decide()
    
    def resistor_output(self):
        power = (self.current**2)*(self.resistance)
        if power > self.power_rating:
            print("Resistor burnt (open circuit) : power({}) > power rating({})".format(round(power,3),self.power_rating))
            self.voltage, self.current = 0, 0

        return self.voltage, self.current
    
    def channel_decide(self):
        # if current_channel is True : the input is in Amps (Current) else in Volts (Voltage)
        if self.current_channel:
            self.conduct_current()
        else:
            self.conduct_voltage()
    
    def conduct_voltage(self):
  
        self.voltage = self.input_
        self.current = self.voltage/self.resistance

    def conduct_current(self):
        self.current = self.input_
        self.voltage = self.current * self.resistance

