import requests

# Define the API endpoint and parameters
url = "https://buzzchat.site/mobile_api/feeds"
params = {
    "session_id": "f83ff083cb07a97b37278ea81eb0194f64cf6feb1680069361a07ea18b639727ba2df76f8a3eaf3994",
    "page_size": 50
}

# Define the keywords to filter the posts
keywords = ["Africa", "Ghana"]

# Make a request to the API endpoint
response = requests.get(url, params=params)

# Check if the API response is successful
if response.status_code == 200:
    # Extract the feed data from the API response
    feed_data = response.json()["data"]["feeds"]
    
    # Sort the feeds in ascending order of the number of likes they have received
    feed_data.sort(key=lambda x: int(x["likes_count"]))
    
    # For each post, check if it contains any of the specified keywords
    for post in feed_data:
        weight = 0
        for keyword in keywords:
            if keyword in post["text"]:
                weight += 1
        
        # Assign a weight to the post based on the number of keywords it contains
        post["weight"] = weight
    
    # Sort the posts again in descending order of their assigned weight
    feed_data.sort(key=lambda x: x["weight"], reverse=True)
    
    # Display the filtered posts in the order they were sorted
    for post in feed_data:
        print(post["text"], "Likes:", post["likes_count"], "Weight:", post["weight"])
else:
    print("API request failed with status code", response.status_code)
