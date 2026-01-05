%matplotlib inline

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

n_qubits = 3
shots = 1000

qc = QuantumCircuit(n_qubits)

qc.h(range(n_qubits))

qc.measure_all()

simulator = AerSimulator()
tqc = transpile(qc, simulator)

job = simulator.run(tqc, shots=shots)
result = job.result()

counts = result.get_counts()
print("Results:", counts)

plot_histogram(counts).show()
