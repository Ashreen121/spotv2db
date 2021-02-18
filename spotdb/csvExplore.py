import pandas as pd


df = pd.read_csv("db.csv")
df.to_html("tableHTML.html")