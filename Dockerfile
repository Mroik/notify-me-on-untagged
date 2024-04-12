FROM python:alpine3.19
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py
