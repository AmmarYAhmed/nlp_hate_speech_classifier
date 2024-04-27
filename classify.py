import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    best_model = joblib.load('best_classifier.pt')
    vectorizer = joblib.load('vectorizer.pt')

    for year in range(2017, 2019):
        print(f'Predicting for {year}...')
        tweets_df = pd.read_csv(f'{year}_tweets.csv', names=['text', 'created_at'])
        tweets_vectorized = vectorizer.transform(tweets_df['text'])

        racism_predictions = best_model.racism_classifier.predict(
            tweets_vectorized)
        sexism_predictions = best_model.sexism_classifier.predict(
            tweets_vectorized)
        xenophobia_predictions = best_model.xenophobia_classifier.predict(
            tweets_vectorized)

        with open(f'{year}_predictions.csv', 'w') as f:
            f.write('created_at,racism,sexism,xenophobia\n')
            for i in range(1, len(tweets_df)):
                f.write(
                    f'{tweets_df["created_at"][i]}, {racism_predictions[i]}, {sexism_predictions[i]}, {xenophobia_predictions[i]}\n')
                
    for year in range(2020, 2024):
        print(f'Predicting for {year}...')
        tweets_df = pd.read_csv(f'{year}_tweets.csv', names=['text', 'created_at'])
        tweets_vectorized = vectorizer.transform(tweets_df['text'])

        racism_predictions = best_model.racism_classifier.predict(
            tweets_vectorized)
        sexism_predictions = best_model.sexism_classifier.predict(
            tweets_vectorized)
        xenophobia_predictions = best_model.xenophobia_classifier.predict(
            tweets_vectorized)

        with open(f'{year}_predictions.csv', 'w') as f:
            f.write('created_at,racism,sexism,xenophobia\n')
            for i in range(1, len(tweets_df)):
                f.write(
                    f'{tweets_df["created_at"][i]}, {racism_predictions[i]}, {sexism_predictions[i]}, {xenophobia_predictions[i]}\n')

if __name__ == '__main__':
    main()
