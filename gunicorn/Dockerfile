FROM python:3
ADD myapp.py /
RUN pip install gunicorn
RUN pip install flask
CMD [ "gunicorn", "-w 1", "--bind=0.0.0.0:9999", "myapp:app" ]