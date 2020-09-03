#!/usr/bin/env python
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute


reg = QuantumRegister(1)


circuit = QuantumCircuit(reg)
circuit.i(reg[0])


simulator = Aer.get_backend("statevector_simulator")
state_vector = execute(circuit, simulator).result().get_statevector()


print()
print(state_vector)
print(circuit.draw())

