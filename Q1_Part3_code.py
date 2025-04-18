import pennylane as qml
from pennylane import numpy as np

# Setting up a 2-qubit device
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit():

    # Applying Hadamard gate to qubit 0
    qml.Hadamard(wires=0)

    # Applying Hadamard and then Pauli-Z gate to qubit 1
    qml.Hadamard(wires=1)
    qml.PauliZ(wires=1)

    return qml.state()

# Drawing the circuit to visualize what is happening
print("Quantum circuit diagram:")
print(qml.draw(circuit)())

# Running the circuit and displaying the resulting quantum state
state = circuit()
print("\nFinal statevector:")
print(state)