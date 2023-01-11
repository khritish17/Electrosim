# ELECTROSIM
Official Documentation of the ELECTROSIM
> **Note** The project is currently active, there may be some updates where old API may be changed according to the requirement. Hence always look out for updates. Onces the project gets finalized this NOTE will be removed. 
### Description:

A simulation of electronics component using python

### Prerequisites

- Install latest version of python, make sure to install the PIP pipeline 
- Install numpy library

### Installation

- Clone the project from [GITLINK](https://github.com/khritish17/Electrosim.git)

### Contact

Author: Khritish Kumar Behera

Email: 
<khritish.official[at]gmail.com>


# ELECTROSIM API

## resistors(*resistance*, *input*, *power_rating*, *current_channel*) | return type: (voltage, current)
The <kbd>resistors</kbd> API, creates a resistor object which requires the following as function parameters:
- **resistance** : It is the resistance of the resistor, should be in SI unit (in Ohms)
- **input** : The input given to the resistor, can be a voltage input (in Volts) or a current input (in Amps)
- **power_rating** : The power rating (in Watts) of the resistor above which the resistor burns, default value is set to 0.125 Watts
- **current_channel** : It's a boolean parameter, which suggests the given *input* is in Volts or Amps, default value is set to False

The output of the <kbd>resistors</kbd> API is the voltage and current

Testing:

    import electrosim as ele
    volts, curr = ele.resistors(resistance= 20, input_ = 0.5)
    print("Votage : {} V".format(volts))
    print("Current : {} A".format(curr))

Output:

    Votage : 0.5 V
    Current : 0.025 A

### When the power gets above the power rating, the function issues a "Resistor burnt" error and makes the resistor open circuit

    import electrosim as ele
    volts, curr = ele.resistors(resistance= 20, input_ = 2)
    print("Votage : {} V".format(volts))
    print("Current : {} A".format(curr))

Output:

    Resistor burnt (open circuit) : power(0.2) > power rating(0.125)
    Votage : 0 V
    Current : 0 A

### Changing the power rating of the resistor

    import electrosim as ele
    volts, curr = ele.resistors(resistance= 20, input_ = 2, power_rating = 0.3)
    print("Votage : {} V".format(volts))
    print("Current : {} A".format(curr))

Output:

    Votage : 2 V
    Current : 0.1 A
