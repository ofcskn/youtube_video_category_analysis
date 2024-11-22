import json
import matplotlib.pyplot as plt
from collections import Counter

def plot_sentiment_density(json_data):
    """Creates a graph density analysis to show the proportion of positive, neutral, and negative comments."""
    # Parse JSON data if it's a string
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    # Extract sentiments
    sentiments = [item["sentiment"] for item in data]

    # Count sentiment occurrences
    sentiment_counts = Counter(sentiments)

    # Ensure consistent ordering of categories
    categories = ["Positive", "Neutral", "Negative"]
    counts = [sentiment_counts.get(category, 0) for category in categories]

    # Plot the data
    plt.figure(figsize=(8, 5))
    plt.bar(categories, counts, alpha=0.7)
    plt.title("Sentiment Density Analysis")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Comments")
    plt.xticks(categories)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Show the graph
    plt.show()