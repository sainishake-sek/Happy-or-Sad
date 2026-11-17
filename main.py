happy_words = ["happy", "joy", "love", "great", "awesome", "good", "excited", "wonderful"]
sad_words = ["sad", "cry", "hate", "bad", "depressed", "lonely", "upset", "terrible"]

sentence = input("Enter a sentence: ").lower()

happy_score = sum(word in sentence for word in happy_words)
sad_score = sum(word in sentence for word in sad_words)

if happy_score > sad_score:
    print("Prediction: Happy")
elif sad_score > happy_score:
    print("Prediction: Sad")
else:
    print("Prediction: Neutral")
