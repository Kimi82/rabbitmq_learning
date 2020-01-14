#FIRST
FROM python:3
ADD emit_log.py .
RUN pip pika install
EXPOSE 8081
EXPOSE 8001
CMD ["python3", "emit_log.py"]


#Second
FROM python:3
ADD receive.py .
RUN pip pika install
EXPOSE 8082
EXPOSE 8002
CMD ["python3", "receive.py"]
