FROM selenium/standalone-chrome

WORKDIR /app

COPY . /app

RUN pip3 install selenium

CMD [ "python3","script.py" ]
