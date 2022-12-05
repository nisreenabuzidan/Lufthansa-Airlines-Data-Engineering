
FROM debian:latest
WORKDIR /app/
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install requests
RUN pip3 install pandas
RUN pip3 install pymongo
RUN pip3 install utils
RUN pip install dash
CMD python3 main.py
