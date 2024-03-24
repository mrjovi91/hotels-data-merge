FROM python:3.11

RUN mkdir /controllers
RUN mkdir /integrations
RUN mkdir /model
RUN mkdir /routes
RUN mkdir /settings
 
COPY controllers /controllers
COPY integrations /integrations
COPY model /model
COPY routes /routes
COPY settings /settings
COPY api.py .
COPY requirements.txt .
COPY wsgi.py .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app