class Model:
    def __init__(self, joblib_model):
        self.predictor = joblib_model
        self.prediction = 0
        self.proba = 0
        self.threshold = 0.4

    def Predict(self, data):
        self.prediction = (
            self.predictor.predict_proba(data)[:, 1].astype(float)[0] > self.threshold
        )
        return self.prediction

    def PredictProb(self, data):
        self.proba = self.predictor.predict_proba(data)[:, 1].astype(float)[0]
        return self.proba

    def MakeRaport(self):
        print(
            f"-----------------RAPORT-----------------\nPrediction: {"Fake" if self.prediction == False else "Real"}\nProbability of prediction: {round((self.proba) * 100,2)}%\nThreshold: {self.threshold}\n----------------------------------------"
        )
