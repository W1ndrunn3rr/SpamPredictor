import spacy
from spacy import displacy


class DataProcessing:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text):
        doc = self.nlp(text)
        for token in doc:
            print(token.vector)


dp = DataProcessing()

dp.process_text("Apple is looking at buying U.K. startup for $1 billion")
