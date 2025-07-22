weather = input("What's the weather like today? (sunny, rainy, cold): windy:"). lower()
recommendations = {
    "sunny": "Wear a t-shirt and sunglasses.",
    "rainy": "Take an umbrella and a rain coat.",
    "cold": "Wear a warm coat and a scarf."
}
if weather in recommendations:
    print(recommendations[weather])
else:
    print("Sorry, I don't have recommendations for this weather.")
