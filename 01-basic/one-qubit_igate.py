#!/usr/bin/env python
import qiskit


reg = qiskit.QuantumRegister(1)


circuit = qiskit.QuantumCircuit(reg)
circuit.i(reg[0])


simulator = qiskit.Aer.get_backend("statevector_simulator")
state_vector = qiskit.execute(circuit, simulator).result().get_statevector()


print()
print(state_vector)
print(circuit.draw())

