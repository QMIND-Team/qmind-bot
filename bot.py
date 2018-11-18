import os
import re
import time
from commands import help_me
from commands import get_gif
from dotenv import load_dotenv
from slackclient import SlackClient

# Load environment variables
load_dotenv()

# initialize Slack Client
slack_client = SlackClient(os.environ.get('BOT_OAUTH_TOKEN'))
starterbot_id = None

#Get API key for giphy
giphy_api_key = os.environ.get("BOT_GIPHY_API_KEY")

# constants
RTM_READ_DELAY = 1
HELP_COMMAND = "help"
GIF_COMMAND = "gif"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None


def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel):
    # Default response is help text for the user
    default_response = f"Howdy :sad_cowboy:! I'm geoff, the QMIND Bot that makes your lives easier. Try me out by using a command like *{HELP_COMMAND} or {GIF_COMMAND}*!"

    # Finds and executes the given command, filling in response
    response = None
    if command.startswith(HELP_COMMAND):
        response = help_me(command)

    elif command.startswith(GIF_COMMAND):
        response = get_gif.get_gif(command, giphy_api_key)

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False, auto_reconnect=True):
        print("Starter Bot connected and running!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while(True):
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. See above for exception")
