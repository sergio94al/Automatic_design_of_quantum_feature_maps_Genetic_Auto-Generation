# Automatic Design of Quantum Feature Maps:  Auto-generated Quantum-Inspired Kernels by using Multi-Objetive Genetic Algorithms (AQIK)

This is the official code of the paper published on August 19, 2021: S. Altares-López, A. Ribeiro, J.J. García-Ripoll, *Automatic design
of quantum feature maps*, Quantum Science and Technology, vol. 6, no. 4, 2021 [1]. 

DOI: https://doi.org/10.1088/2058-9565/ac1ab1

* This work has also been presented in the *2nd European Quantum Technologies Conference* (Virtual Conference, Dublin, Ireland) in Poster format: https://az659834.vo.msecnd.net/eventsairwesteuprod/production-abbey-public/9641064fd4a342ab9c4d81cf221ac4dd

### Abstract

We propose a new technique for the **automatic generation of optimal ad-hoc ansätze for classification by using quantum support vector machine**. This efficient method is based on NSGA-II multiobjective genetic algorithms which allow both maximize the accuracy and minimize the ansatz size. It is demonstrated the validity of the technique by a practical example with a non-linear dataset, interpreting the resulting circuit and its outputs. We also show other application fields of the technique that reinforce the validity of the method, and a comparison with classical classifiers in order to understand the advantages of using quantum machine learning.


## Goals of the Technique

* Maximize Accuracy.
* Minimize quantum classifier size, in terms of quantum gates, layers and number of qubits, thus, reducing the expressivity of the quantum circuits.
* Take into account the **use case**, generating **ad-hoc classifiers** for each data set.
* Generate an automatic and optimized system for data encoding of classical information into the quantum feature maps.
* Optimization of the circuit structure, gate types and its parameters *θ*.
* Find robustness classifiers with a high generalization power.
* Search of quantum-inspired solutions that can be implemented on classical computers.
* Provide interpretability to the predicted results.

## Genetic Quantum Feature Maps: Technique

In this paper we propose a novel technique for **quantum machine learning** (QML) which allows for tabular datasets the **automatic generation of quantum-inspired kernels for classification** by using Quantum Support Vector Machine (QSVM), based on Multi-Objective Genetic Algorithms (MO-GA).

<p align="center">
  <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/General_tech.png" width="500" height="400">
</p>

The goal of the technique is to achieve the quantum circuit that provides the **best accuracy** on test data, as well as the **smallest ansatz size**. Since the objective of the fitness function is the test accuracy, we force the circuits-solution to be robust and to **avoid overfitting effects, being quantum classifiers with a high generalization power**. 

Taking into account the ansatz size, our goal is to minimize it as much as possible in order to have solutions that avoid expressivity problems. This is possible because we code identity gates, which allows the **possibility of eliminating gates, layers and even reduce the number of qubits in the circuits**.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/Ansatz_build.png" width="500" height="350">
</p>

 In addition, we penalize the occurrence of CNOT (entangling gates), in order to achieve solutions with **lower computational cost and quantum-inspired machine learning solutions**, by using the following expression.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/Size_metric.png" width="325" height="60">
</p>

## Multi-Objetive Genetic Algorithm (MO-GA)

These are algorithms allow the exploration of large solution spaces in order to find the most optimal or closest solutions, since the methodology is meta-heuristic [2]. Since we have two objectives, we use **NSGA-II algorithm and Pareto Front, in order to find and save the non-dominated solutions** [3]. Those solutions that, improve one of the two objectives without getting worse results in the other effort metric are saved. In order to provide a **higher degree of elitism** to the technique, we use the *μ+λ* algorithm, which face parents against their offspring, keeping the best individuals for the following generations.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/GA.png" width="550" height="400">
</p>

* **Step 1**: A starting population is created -Initial population. In our case individuals are binary strings.

* **Step 2**: These individuals are evaluated in a **fitness function**. The output of this function will determine whether the individual is accurate for the given problem or not. In the proposed technique, the **binary strings are converted into quantum circuits** which will act as feature maps into QSVM. Firstly, the classifier is fitted with training set and then we make predictions over test set **-searching generalization power-**, getting the objetive of the fitness function.  At the same time, we calculate the number of gates and we calculate a metric -Weight Control- in order to find a **balance between both metrics**, the accuracy and the reduction of number of gates. It is important since a high weight on the reducing circuit size objetive can lead less accuracy because of information loss.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/Wcontrol.png" width="400" height="30">
</p>

* **Step 3**: We select the best individuals. We apply **genetic operators** of crossover (Two-points) and mutation (Flipbit), generating new individuals (offspring) for the next generation. These operators are applied with a probability *Pm* and *Pc* respectively. The mutation operator allows us to reach other points in the search space since it allows us to **avoid local minima**, making the search for the best solution more efficient.

* **Step 4**: The process is repeated until convergence or when stop conditions are achieved.

## Interpretability of Results

Once the evolution is finished, we obtain the **optimized quantum circuit** with the best test accuracy - thus ensuring that there is no overfitting on the train data, being classifiers with a high generalization power and robustness - and with the lowest number of quantum gates and qubits for non-linear datasets [6].

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/DS.png" width="350" height="220">               <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/Optimized quantum feature map - moons.png" width="350" height="220">
</p>

The resulting quantum circuit can be decomposed by qubits because there are no entangling gates among them. **Each qubit constitutes its own kernel**. We note that when we evaluate each qubit separately does not provide a high accuracy for this non-linear dataset [6], as can be seen in the decision boundaries (b-d). However, the **combination of all kernels produces a prediction of 1.0 in test data** (a) with the next expression:

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/kernel.png" width="220" height="25">
</p>

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/Qubits_Interpretability.png" alt='qubits vs. quantum circuit' width="500" height="325">   
</p>

## Other Insights

By using this technique, we are able to include **many variables in few qubits**, because the genetic algorithm takes into account the possibility of combining more than one variables per qubits as in the Parkinson's example [5]. In this use case 22 variables are included in 8 qubits, **decreasing considerably the expressivity of the circuits-solution**.

<p align="center">
    <img src="https://github.com/sergio94al/Automatic-design-of-quantum-feature-maps/blob/main/Images/park.png" alt='qubits vs. quantum circuit' width="500" height="300"> 
</p>

## Files Description

* circuit.py: We create the quantum operators that will composed the quantum circuit.
* fitness.py: Evaluation fuction of the genetic algorithm (we fit 2 variables to return -the objetives)
* gsvm.py: Genetic algorithm function with the genetic operators. We call the fitness function.
* qsvm.py: We create a simulated quantum support vector machine by using sklearn.
* encoding.py: In this file we create the encoding of the quantum gates and the parameters *θ*.
* encoding2.py: This file is used to visualize the solution after the evolution.

#### Notebook - Use case Folder:
* Sample_Usecase.ipynb: Notebook used to launch the quantum feature maps' evolution, and save the best individuals which appear along the evolution in an excel file, so it can be decoded into a quantum circuit. 
* sample_iot_data.csv: Dataset free available on Kaggle. Used as an example [4].
* sample_iot_result_n5.csv: Output file with the best individuals in the evolution. The structure of the file is:  *ID  |  Individual (quantum classifier) to be decoded | Weight control metric | Accuracy on test set*


## How to Cite

Authors of scientific papers including results generated using this technique or these ideas, are encouraged to cite the following paper:

* Altares-López, S., Ribeiro, A., & García-Ripoll, J. J. (2021). Automatic design of quantum feature maps. Quantum Science and Technology, 6(4), 045015. https://doi.org/10.1088%2F2058-9565%2Fac1ab1
```xml
@article{altares2021automatic,
  title={Automatic design of quantum feature maps},
  author={Altares-L{\'o}pez, Sergio and Ribeiro, Angela and Garc{\'\i}a-Ripoll, Juan Jos{\'e}},
  journal={Quantum Science and Technology},
  volume={6},
  number={4},
  pages={045015},
  year={2021},
  doi = {10.1088/2058-9565/ac1ab1},
  url = {https://doi.org/10.1088%2F2058-9565%2Fac1ab1},
  publisher={IOP Publishing}
}

```
## References

* [1] S. Altares-López, A. Ribeiro, J.J. García-Ripoll, *Automatic design of quantum feature maps*, Quantum Science and Technology, vol. 6, no. 4, 2021. https://doi.org/10.1088/2058-9565/ac1ab1
* [2] De Rainville, F. M., Fortin, F. A., Gardner, M. A., Parizeau, M., & Gagné, C. (2012, July). *Deap: A python framework for evolutionary algorithms*. In Proceedings of the 14th annual conference companion on Genetic and evolutionary computation (pp. 85-92). https://doi.org/10.1145/2330784.2330799
* [3] Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. A. M. T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE transactions on evolutionary computation, 6(2), 182-197. DOI: 10.1109/4235.996017

#### Datasets

* [4] Patel H 2020 Intelligent irrigation system (by using temperature and moisture data) - Kaggle Dataset. https://www.kaggle.com/harshilpatel355/autoirrigationdata
* [5] Little, M., Mcsharry, P., Roberts, S., Costello, D., & Moroz, I. (2007). Exploiting nonlinear recurrence and fractal scaling properties for voice disorder detection. Nature Precedings, 1-1.
* [6]  Thirion B, Varoquaux G, Gramfort A, Michel V, Grisel O, Louppe G and Nothman J scikit-datasets (generate samples of synthetic data sets). URL https://github.com/scikit-learn/scikit-learn

