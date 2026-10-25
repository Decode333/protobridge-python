from src.data.load_data import load_data
 
df = load_data("data/raw/Reviews.csv")
 
print(df.head())
print(df.columns)