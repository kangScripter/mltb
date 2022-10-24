FROM anasty17/mltb:latest

WORKDIR /usr/src/app

RUN chmod 777 /usr/src/app

RUN apt-get install firefox

RUN apg-get install google-chrome

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
