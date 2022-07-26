# Automatic design of quantum feature maps: Genetically designed Quantum-Inspired Kernels

This is the official code of the paper published on August 19, 2021: S. Altares-López, A. Ribeiro, J.J. García-Ripoll, Automatic design
of quantum feature maps, Quantum Science and Technology, vol. 6, no.4, 2021. 

DOI: https://doi.org/10.1088/2058-9565/ac1ab1

## Genetic-Quantum Feature Maps: Technique

In this paper we propose a novel technique that allows the automatic generation of quantum circuits that function as quantum feature maps in QSVM for classification, based on multi-objective genetic algorithms.

<p align="center">
  <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/General_tech.png" width="500" height="400">
</p>

The goal of the technique is to achieve the quantum circuit that provides the best test data accuracy, as well as the smallest ansatz size. As the objective of the fitness function is the test accuracy, we force the circuit to be robust and to avoid overfitting effects. 

Taking into account the ansatz size, our goal is to minimize it as much as possible in order to have solutions that avoid expressibility problems. This is possible because we code identity gates, which allows the possibility of eliminating gates, layers and even number of qubits in the circuits.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Ansatz_build.png" width="400" height="250">
</p>

 In addition, we penalize the occurrence of CNOT (entangling gates), in order to achieve solutions with lower computational cost and quantum-inspired solutions, by using the following expression.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Size_metric.png" width="300" height="150">
</p>

## Genetic algorithms (GA)

These are algorithms allow the exploration of large solution spaces in order to find the most optimal or closest solutions, since the methodology is meta-heuristic. Since we have two objectives, we use Pareto Front in order to save the best non-dominated solutions. Those solutions that, improve one of the two objectives without getting worse results in the other effort metric are saved.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/GA.png" width="450" height="300">
</p>

* **Step 1**: A starting population is created -Initial population. In our case individuals are binary strings.

* **Step 2**: This population is evaluated in a fitness function. The output of this function will determine whether the individual is accurate for the given problem or not. In the proposed technique, the binary strings are converted into quantum circuits which will act as feature maps into QSVM. First the classifier is fitted with training set and then we make predictions over test set, getting the objetive of the fitness function.  At the same time, we calculate the number of gates and we calculate a metric -Weight Control- in order to find a balance between the accuracy and the reduction of number of gates.

* **Step 3**: We select the best individuals. We apply genetic operators of crossover (Two-points) and mutation (Flipbit), generating new individuals (offspring) for the next generation. The mutation operator allows us to reach other points in the search space since it allows us to avoid local minima, making the search for the best solution more efficient.

* **Step 4**: The process is repeated until convergence or when stop conditions are achieved.

## Interpretability of results

Once the evolution is finished, we obtain the optimized quantum circuit with the best test accuracy - thus ensuring that there is no overfitting on the train data and that there is generalization and robustness in the quantum classifier - and with the lowest number of quantum gates.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/DS.png" width="250" height="150">               <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Optimized quantum feature map - moons.png" width="250" height="150">
</p>

The resulting circuit can be decomposed by qubits because there are no entangling gates among them. We note that each qubit separately does not provide a high accuracy, however, the combination of all kernels produces a prediction of 1.0 in test data.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Qubits_Interpretability.png" alt='qubits vs. quantum circuit' width="400" height="250">   
</p>


## Files description

* circuit.py: We create the quantum operators
* fitness.py: Evaluation fuction of the genetic algorithm (we fit 2 variables to return -the objetives)
* gsvm.py: Genetic algorithm function in order. We call the fitness function
* qsvm.py: We create a simulated quantum support vector machine by using sklearn.
* encoding.py: In this file we create the encoding of the quantum gates and the parameters θ.
* encoding2.py: This file is used to visualize the solution after the evolution.
* Sample_Usecase.ipynb: Notebook used to initialize and save the best population in the evolution in excel, so it can be decoded into a quantum circuit.

## References

* S. Altares-López, A. Ribeiro, J.J. García-Ripoll, Automatic design of quantum feature maps, Quantum Science and Technology, vol. 6, no.4, 2021. https://doi.org/10.1088/2058-9565/ac1ab1
