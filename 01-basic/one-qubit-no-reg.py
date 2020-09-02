#!/usr/bin/env python
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute



circuit = QuantumCircuit(1)


simulator = Aer.get_backend("statevector_simulator")
job = execute(circuit, simulator)


result = job.result()
statevector = result.get_statevector()
print(statevector)


print(circuit.draw())

