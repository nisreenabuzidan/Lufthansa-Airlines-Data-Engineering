
FROM debian:latest
WORKDIR /app/
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install requests
RUN pip3 install pandas
RUN pip3 install pymongo
RUN pip3 install utils
#RUN python3.10 -m pip install --upgrade pip
CMD python3 main.py
