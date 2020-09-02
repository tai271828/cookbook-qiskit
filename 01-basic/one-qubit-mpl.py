#!/usr/bin/env python
import matplotlib.pyplot as plt
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute


q = QuantumRegister(1)
circuit = QuantumCircuit(q)


simulator = Aer.get_backend("statevector_simulator")
job = execute(circuit, simulator)


result = job.result()
statevector = result.get_statevector()
print(statevector)


circuit.draw(output="mpl")
plt.show()

