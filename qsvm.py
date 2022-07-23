from sklearn.svm import SVC

class QSVM:

    def __init__(self, feature_map, train_features, train_label):
        def kernel(x1, x2):
            ψ1 = feature_map(x1.T)
            ψ2 = feature_map(x2.T)
            gram = ψ1.real @ ψ2.real.T + ψ1.imag @ ψ2.imag.T
            return gram
        self.svc = SVC(kernel=kernel)
        self.svc.fit(train_features, train_label)

    def run(self):
        pass

    def predict(self, dataset_features):
        return self.svc.predict(dataset_features)
