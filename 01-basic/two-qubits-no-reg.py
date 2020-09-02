#!/usr/bin/env python
import matplotlib.pyplot as plt
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute



circuit = QuantumCircuit(2)


simulator = Aer.get_backend("statevector_simulator")
job = execute(circuit, simulator)


result = job.result()
statevector = result.get_statevector()
print(statevector)


print(circuit.draw())

