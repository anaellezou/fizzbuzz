FROM python:3.7.9

COPY ./requirements.txt /fizzbuzz/requirements.txt

WORKDIR /fizzbuzz

RUN pip install -r requirements.txt

COPY . /fizzbuzz

ENTRYPOINT [ "python" ]

CMD [ "fizzbuzz.py" ]
