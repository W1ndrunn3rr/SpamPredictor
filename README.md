# FAKE NEWS PREDICTOR - SUPERVISED MACHINE LEARNING PROJECT

## 1. DESCRIPTION

This project is a supervised machine learning project that aims to predict whether a news is fake or real. The dataset used in this project is a collection of news articles from various sources taken from github repo of Sophia Latessa.The project uses the Extra Forest Classifier from Scikit-Learn library and SpaCy and Asent Library to process text using NLP techniques. In this project, the news articles are preprocessed and converted into a format that can be used by the Extra Forest Classifier to predict whether a news is fake or real based on the features extracted from the news articles.

## 2. DATASET

Project generates a dataframe with the following features:

- `title`: The title of the analyzed text.
- `neg_score`: Negative sentiment score (rounded to 3 decimal places).
- `neu_score`: Neutral sentiment score (rounded to 3 decimal places).
- `pos_score`: Positive sentiment score (rounded to 3 decimal places).
- `compound_score`: Overall compound sentiment score (rounded to 3 decimal places).
- `n_sentences`: Number of sentences in the text.
- `n_tokens`: Total number of tokens (words) in the text.
- `unique_tokens_r`: Ratio of unique tokens to total tokens (rounded to 3 decimal places).
- `nouns_r`: Ratio of nouns to total words (rounded to 3 decimal places).
- `proper_nouns_r`: Ratio of proper nouns to total words (rounded to 3 decimal places).
- `verbs_r`: Ratio of verbs to total words (rounded to 3 decimal places).
- `adverbs_r`: Ratio of adverbs to total words (rounded to 3 decimal places).
- `adjectives_r`: Ratio of adjectives to total words (rounded to 3 decimal places).
- `news`: Label indicating the classification of the text.

This dataframe provides a comprehensive analysis of the text, including sentiment scores, linguistic features, and classification results.

## 3. INSTALLATION

For installation type in terminal :

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
pip install -r requirements.txt
```
To clone the repository and install the required packages.

## 4. USAGE

To run the project, type in terminal:

```bash
python3 main.py <url_or_text>
```
where `<url_or_text>` is the URL of the news article or the text to be analyzed. The project will then process the text and output the classification results in the form of a report.

## 5.FEATURES

- Sentiment Analysis
- Supervised Machine Learning
- Text Preprocessing
- Feature Extraction
- Classification
- Report Generation

## 6. CONTRIBUTING

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 7. LICENSE

[MIT](https://choosealicense.com/licenses/mit/)

## 8.DEPENDENCIES

This project requires the following Python packages:

- requests
- beautifulsoup4
- spacy
- scikit-learn
- asent
- pandas
- joblib
- validators

## 9. DATA SOURCE

The dataset used in this project is a collection of news articles from various sources taken from the following github repo: https://github.com/sophialatessa/FakeNewsDeepLearning

## DISCLAIMER

This project is for hobby and educational purposes only. It should not be used as a basis for any decisions or actions. The project analyzes patterns in texts and does not verify the accuracy of information. Always verify information from reliable sources and check for proper authorization to ensure accuracy and avoid misinformation or fake news.
