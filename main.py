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

    predictor = joblib.load("data/predictor.pkl")

    model = Model(predictor, dataframe)

    model.MakeRaport(
        data,
        dataframe,
        source=(
            scrapper.url if validators.url(parser.parse_args().data) else "User input"
        ),
    )


if __name__ == "__main__":
    main()
