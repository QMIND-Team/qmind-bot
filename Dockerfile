FROM ubuntu:16.04

# Install Dependencies
RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y wget
RUN apt-get install firefox --yes

# Update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

# Initialize app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Download geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
RUN sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
RUN chmod +x /usr/bin/geckodriver
RUN rm geckodriver-v0.23.0-linux64.tar.gz
COPY . /app
CMD python3.6 bot.py
