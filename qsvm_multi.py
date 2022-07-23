from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier,OneVsOneClassifier

#OneVsRestClassifier also known as one-vs-all.
#OneVsOneClassifier constructs one classifier per pair of classes.



class QSVM:

    def __init__(self, feature_map, train_features, train_label):
        def kernel(x1, x2):
            ψ1 = feature_map(x1.T)
            ψ2 = feature_map(x2.T)
            gram = ψ1.real @ ψ2.real.T + ψ1.imag @ ψ2.imag.T
            return gram
        self.multi_svc = OneVsOneClassifier(SVC(kernel=kernel, decision_function_shape = 'ovo'))
        self.multi_svc.fit(train_features, train_label)

    def run(self):
        pass

    def predict(self, dataset_features):
        return self.multi_svc.predict(dataset_features)
