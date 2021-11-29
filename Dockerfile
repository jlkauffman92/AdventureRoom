FROM python:3.7
ADD . /AdventureRoom
WORKDIR /mnt/i/Dev/AdventureRoom
RUN pip install flask
CMD flask run -h 0.0.0.0 -p 5000
