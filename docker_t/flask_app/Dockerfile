FROM python:3.9 

WORKDIR /app 

COPY . /app    

RUN pip3 install -r requirements.txt 

EXPOSE 5000 

CMD ['python3','app.py']

#docker build -t flask_app . 

#docker run -p 5000:5000 flask_app 