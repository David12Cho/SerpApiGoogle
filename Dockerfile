FROM python:3.9

ADD serp.py .

RUN  pip3 install requests google-search-results

ENV PYTHONPATH /code

CMD [ "python", "./serp.py" ]
