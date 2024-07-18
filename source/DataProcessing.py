import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import asent
import pandas as pd
from source import Scrapper


class DataProcessing:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe("sentencizer")
        self.nlp.add_pipe("asent_en_v1")

        self.wordDict = {"NOUN": 0, "PROPN": 0, "VERB": 0, "ADJ": 0, "ADV": 0}
        self.uniqueTokens = set()
        self.sentimentalScore = None
        self.tokens = 0

    def ProcessText(self, text):
        doc = self.nlp(text)
        tokens = [
            token.text.lower() for token in doc if token.pos_ in self.wordDict.keys()
        ]
        self.tokens = len(tokens)

        tokens = [token for token in tokens if len(token) > 2]

        for token in doc:
            if token.pos_ in self.wordDict.keys():
                self.wordDict[token.pos_] += 1

        self.uniqueTokens.update(tokens)

        self.sentimentalScore = doc._.polarity

    def ProcessData(self):
        total_w = sum(
            self.wordDict.get(tag, 0) for tag in ["NOUN", "PROPN", "VERB", "ADV", "ADJ"]
        )

        dataframe = {
            "neg_score": (
                round(self.sentimentalScore.negative, 3)
                if self.sentimentalScore is not None
                else 0
            ),
            "neu_score": (
                round(self.sentimentalScore.neutral, 3)
                if self.sentimentalScore is not None
                else 0
            ),
            "pos_score": (
                round(self.sentimentalScore.positive, 3)
                if self.sentimentalScore is not None
                else 0
            ),
            "compound_score": (
                round(self.sentimentalScore.compound, 3)
                if self.sentimentalScore is not None
                else 0
            ),
            "n_sentences": (
                self.sentimentalScore.n_sentences
                if self.sentimentalScore is not None
                else 0
            ),
            "n_tokens": self.tokens,
            "unique_tokens_r": (
                round(len(self.uniqueTokens) / self.tokens, 3) if self.tokens > 0 else 0
            ),
            "nouns_r": round(self.wordDict["NOUN"] / total_w, 3) if total_w > 0 else 0,
            "proper_nouns_r": (
                round(self.wordDict["PROPN"] / total_w, 3) if total_w > 0 else 0
            ),
            "verbs_r": round(self.wordDict["VERB"] / total_w, 3) if total_w > 0 else 0,
            "adverbs_r": round(self.wordDict["ADV"] / total_w, 3) if total_w > 0 else 0,
            "adjectives_r": (
                round(self.wordDict["ADJ"] / total_w, 3) if total_w > 0 else 0
            ),
            "article_tone": (
                self.sentimentalScore.compound + self.sentimentalScore.neutral
                if self.sentimentalScore is not None
                and self.sentimentalScore.compound > 0
                else 0
            ),
            "mean_sentence_length": (
                self.tokens / self.sentimentalScore.n_sentences
                if self.sentimentalScore is not None
                and self.sentimentalScore.n_sentences > 0
                else 0
            ),
        }
        df = pd.DataFrame(dataframe, index=[0]).reset_index(drop=True)

        return df
