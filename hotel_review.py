import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()

data = pd.read_csv("hotel_reviews.csv")
print(data.head())

ratings = data["reviews.rating"].value_counts()
numbers = ratings.index
quantity = ratings.values

custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(5, 5))
plt.pie(quantity, labels=numbers, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Hotel Reviews Ratings", fontsize=20)
plt.show()

sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores((u",i,"))["pos"] for i in data["Reviews"]]
data["Negative"] = [sentiments.polarity_scores((u",i,"))["neg"] for i in data["Reviews"]]
data["Neutral"] = [sentiments.polarity_scores((u",i,"))["neu"] for i in data["Reviews"]]
print(data.head())

x = sum(data["Positive"])
y = sum(data["Negative"])
z = sum(data["Neutral"])

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print("Positive 😊 ")
    elif (b>a) and (b>c):
        print("Negative 😠 ")
    else:
        print("Neutral 🙂 ")
sentiment_score(x, y, z)

print("Positive: ", x)
print("Negative: ", y)
print("Neutral: ", z)