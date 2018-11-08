# QMIND-Bot

This repository is the home of Geoff, QMIND's very own Slack Bot. Geoff has very limited functionality at the moment, but hopefully that will change with the help of the QMIND Team!

# Usage

To work on Geoff, you will need the following requirements:

- Python 3.x
- Docker

To run locally simply use the following commands:

```bash
git clone https://github.com/QMIND-Team/QMIND-bot.git
cd qmind-bot
pip install -r requirements.txt
python bot.py
```

> Note: You will need to fill out a `.env` file matching `.env.example` in the root of your file with Slack API credentials. To obtain these, DM @mcteppcheese on Slack

# Buiding the Docker Container

To run Geoff in a docker container simply run the following commands:

```docker
docker build -t qmind-bot .
docker run -d -p 80 qmind-bot
```

> Note: this will run docker as a daemon

# Contribution

To contribute to Geoff do the following:

- Make a branch - `git checkout -b feature/my-feature`
- Commit your changes - `git commit -am "My changes"`
- Push your changes and make a PR! - `git push -u origin feature/my-feature`
