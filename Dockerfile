FROM ubuntu:20.10

ARG PASSWORD
RUN test -n "$PASSWORD"

ENV login=$PASSWORD

ARG GECKO_LINK=https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz

RUN apt update \
	&& DEBIAN_FRONTEND="noninteractive" apt install -y python3 python3-pip wget firefox \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium

WORKDIR /home

RUN wget -q ${GECKO_LINK} && tar -xvzf geckodriver* && rm geckodriver-* && chmod +x geckodriver 

ENV PATH "$PATH:/home/."

COPY unFirewall.py unFirewall.py



CMD python3 unFirewall.py

#CMD "sh"
