from source import Scrapper, Model, DataProcessing
import argparse
import joblib
import validators


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="URL to scrape or text to process")

    dp = DataProcessing()

    if validators.url(parser.parse_args().data):
        scrapper = Scrapper(parser.parse_args().data)
        scrapper.Scrape()
        data = scrapper.content
    else:
        data = parser.parse_args().data

    dp.ProcessText(data)

    dataframe = dp.ProcessData()

    print(dataframe)

    predictor = joblib.load("data/predictor.pkl")

    model = Model(predictor)

    proba = model.PredictProb(dataframe)
    prediction = model.Predict(dataframe)

    model.MakeRaport()


if __name__ == "__main__":
    main()
