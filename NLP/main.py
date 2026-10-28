# import pandas as pd
#
#
# df = pd.read_csv("data/processed/cleaned_reviews.csv")
#
# print(df.head())
# print(df[df["clean_review"].isnull()])

from src.data.process_dataset import process_dataset

process_dataset()