import pandas as pd
from src.data.preprocess import create_sentiment, clean_batch


def process_dataset():
    print("Script Started")

    df = pd.read_csv("data/raw/Reviews.csv")

    print("Dataset Loaded")

    # Random sample, NOT head() — the file is grouped by product,
    # so the first rows are a narrow slice. random_state keeps it repeatable.
    # df = df.sample(50000, random_state=42)

    df["reviews.text"] = df["reviews.text"].fillna("")
    df["sentiment"] = df["reviews.text"].apply(create_sentiment)

    print("Sentiment Created")

    # Lowercasing + regex are fast as vectorized pandas ops,
    # so we do them here and leave only tokenizing/lemmatizing to spaCy.
    texts = df["reviews.text"].astype(str).str.lower()
    texts = texts.str.replace(r"http\S+", " ", regex=True)
    texts = texts.str.replace(r"[^a-zA-Z]", " ", regex=True)
    texts = texts.str.replace(r"\s+", " ", regex=True)

    df["clean_review"] = clean_batch(texts)

    # Remove missing or blank results before saving the processed dataset.
    df["clean_review"] = df["clean_review"].fillna("").astype(str).str.strip()

    invalid_count = (df["clean_review"] == "").sum()
    print(f"Removing {invalid_count} blank/invalid cleaned reviews")

    df = df[df["clean_review"] != ""].copy()

    print("NaN clean_review after cleanup:", df["clean_review"].isna().sum())

    df = df[["clean_review", "sentiment"]]

    print("Cleaning Completed")

    df.to_csv(

        "data/processed/cleaned_reviews.csv",

        index=False

    )

    print("File Saved")
