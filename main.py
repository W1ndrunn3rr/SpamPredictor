from source import Scrapper
from source.DataProcessing import DataProcessing
import argparse
import joblib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL to scrape")
    scrapper = Scrapper(parser.parse_args().url)
    scrapper.Scrape()
    dp = DataProcessing(scrapper)
    dp.ProcessText()
    dataframe = dp.ProcessURLData()

    print(f"Dataframe: {dataframe}")

    model = joblib.load("data/predictor01.pkl")

    prediction = model.predict_proba(dataframe)[:, 1]
    tag = (prediction > 0.4).astype(int)
    print(prediction, tag)

    # links = [
    #     "https://www.theguardian.com/commentisfree/2016/nov/04/bravo-green-party-richmond-park-byelection-zac-goldsmith",
    #     " https://www.theguardian.com/science/2016/nov/03/worried-well-more-risk-heart-disease-research-finds",
    #     "https://www.theguardian.com/commentisfree/2016/nov/04/hazelwoods-closure-was-inevitable-so-where-was-the-transition-plan",
    #     "https://www.theguardian.com/music/2016/nov/03/bon-jovi-this-house-is-not-for-sale-review",
    #     " https://www.theguardian.com/travel/2016/nov/03/48-hours-in-the-grampians-victoria-mountain-hikes-fine-food-and-live-music",
    #     "https://www.theguardian.com/business/2016/nov/03/all-of-europe-will-suffer-if-london-loses-financial-clout-says-bank-deputy",
    #     "https://www.theguardian.com/sustainable-business/2016/nov/04/opening-doors-for-women-and-children-when-domestic-violence-hits-home",
    #     "https://www.theguardian.com/film/2016/nov/03/the-accountant-review-ben-affleck-superhero",
    #     "https://www.theguardian.com/film/2016/nov/03/richard-linklater-dream-is-destiny-review-documentary",
    #     "https://www.theguardian.com/australia-news/2016/nov/04/latrobe-valley-266m-economic-growth-zone-after-hazelwood-closure",
    #     "https://www.theguardian.com/film/2016/nov/03/the-darkest-universe-review-will-sharpe-tom-kingsley",
    #     "https://www.theguardian.com/stage/2016/nov/03/dead-funny-review-terry-johnson-vaudeville-london-katherine-parkinson-1994-drama",
    #     "https://www.theguardian.com/film/2016/nov/03/rupture-review-torture-porn-horror-noomi-rapace",
    #     " https://www.theguardian.com/football/2016/nov/03/liverpool-michael-edwards-sporting-director-transfers-anfield",
    #     "https://www.theguardian.com/society/2016/nov/03/age-of-onset-for-multiple-sclerosis-linked-to-distance-from-equator",
    # ]

    # for link in links:
    #     scrapper = Scrapper(link)
    #     scrapper.Scrape()
    #     dp = DataProcessing(scrapper)
    #     dp.ProcessText()
    #     dataframe = dp.ProcessURLData()
    #     prediction = model.predict_proba(dataframe)[:, 1]
    #     tag = (prediction >= 0.3).astype(int)
    #     print(f"Prediction for {link}: {tag}")


if __name__ == "__main__":
    main()
