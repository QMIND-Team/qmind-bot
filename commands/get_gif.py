#Gif generation from Giphy for Geoff (slackbot)
import giphy_client
import random
from giphy_client.rest import ApiException

def get_gif(gif_name, api_key):
    # create API class instance
    api_instance = giphy_client.DefaultApi()

    try:
        # Search for 5 gifs (pretty arbitrary, lower to keep search time down)
        api_response = api_instance.gifs_search_get(api_key, gif_name, limit=5, lang="en")
        # If the gif can't be found
        if len(api_response.data) != 5:
            return "Looks like I couldn't find that gif for you :sad_cowboy:"
        # Choose a random gif
        response_num = random.randint(0, 4)
        return f"Here's what I found :face_with_cowboy_hat:\n" \
               f"{api_response.data[response_num].images.downsized.url}"

    except ApiException as e:
        return "Looks like I couldn't find that gif for you :sad_cowboy:"
