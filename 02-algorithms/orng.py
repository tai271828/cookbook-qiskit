#!/usr/bin/env python
from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister, Aer, execute


reg = QuantumRegister(1, name='reg')
reg_c = ClassicalRegister(1, name='regc')
circuit = QuantumCircuit(reg, reg_c)


# the state default will be 0
circuit.reset(reg)
# apply H gate
circuit.h(reg)
# classic bit is required to perform measurement
circuit.measure(reg, reg_c)


simulator = Aer.get_backend('statevector_simulator')
job = execute(circuit, simulator)
result = job.result()


counts = result.get_counts(circuit)
print('counts:', counts)

outputstate = result.get_statevector(circuit)
print(outputstate)
print(circuit.draw())
