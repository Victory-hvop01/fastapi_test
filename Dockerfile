FROM python:3.12.8

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py","--host","0.0.0.0","--port","80"]


