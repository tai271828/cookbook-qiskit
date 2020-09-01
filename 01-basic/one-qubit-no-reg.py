#!/usr/bin/env python
import matplotlib.pyplot as plt
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute

simulator = Aer.get_backend("statevector_simulator")


circuit = QuantumCircuit(1)


job = execute(circuit, simulator)

result = job.result()
statevector = result.get_statevector()
print(statevector)

circuit.draw(output="mpl")
plt.show()

