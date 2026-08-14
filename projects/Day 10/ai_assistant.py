from transformers import pipeline

# Load the pre-trained sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

print("=" * 50)
print("        AI SENTIMENT ASSISTANT")
print("=" * 50)

sentence = input("Enter a sentence: ")

result = sentiment_model(sentence)[0]

label = result["label"]
score = result["score"]

print("\nPrediction")
print("-" * 50)
print("Sentence  :", sentence)
print("Sentiment :", label)
print("Confidence:", round(score * 100, 2), "%")