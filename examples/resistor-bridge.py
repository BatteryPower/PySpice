####################################################################################################

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

####################################################################################################

from PySpice.Netlist import Circuit
from PySpice.Pipe import SpiceServer
from PySpice.Units import *

####################################################################################################

spice_server = SpiceServer()

####################################################################################################

circuit = Circuit('Resistor Bridge')

circuit.V('input', 1, circuit.gnd, 10) # Fixme: V(10) uV(10) 10*V
circuit.R(1, 1, 2, kilo(2))
circuit.R(2, 1, 3, kilo(1))
circuit.R(3, 2, circuit.gnd, kilo(1))
circuit.R(4, 3, circuit.gnd, kilo(2))
circuit.R(5, 3, 2, kilo(2))

simulation = circuit.simulation(temperature=25, nominal_temperature=25)
simulation.operating_point()
print str(simulation)

raw_file = spice_server(simulation)
for field in raw_file.variables:
    print field

analysis = raw_file.analysis
for node in analysis.nodes.itervalues():
    print 'Node {}: {} V'.format(str(node), float(node)) # Fixme: format value + unit

####################################################################################################
# 
# End
# 
####################################################################################################
