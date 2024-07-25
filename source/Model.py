from datetime import datetime


class Model:
    def __init__(self, joblib_model, data):
        self.predictor = joblib_model
        self.proba = self.predictor.predict_proba(data)[:, 1][0]
        self.prediction = False
        self.threshold = 0.4

    def Predict(self):
        self.prediction = self.proba > self.threshold
        return

    def PredictProba(self):
        return self.proba

    def MakeRaport(self, text, data, source="Unknown"):

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        accuracy = 0.8

        report = f"""
        News Analysis Report
        -------------------------
        Date and Time of Analysis: {current_time}

        Analyzed Text: {text}

        Analysis Result: {'Real news' if self.prediction else 'Fake news'}

        Probability:
            - Real news: {self.proba}
            - Fake news: {1-self.proba}

        Source of the message: {source}

        Model Statistics:
            - Model accuracy (estimated): {accuracy*100:.2f}%
            - Model is adjusted to predict with a threshold of {self.threshold} probability.
            - It is possible to adjust the threshold to increase the sensitivity or specificity of the model.

        Recommendations:
            - Verify the message from trusted sources.
            - Consult an expert if in doubt.
        """
        print(report)
