FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# sh -c allows for environment variable usage
CMD [ "sh", "-c", "python ./run.py ${pgn}" ] 
