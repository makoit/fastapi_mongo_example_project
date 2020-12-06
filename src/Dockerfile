#base image
FROM python:3.8

# sent python output straight to terminal (container log)
ENV PYTHONUNBUFFERED 1

#add backend folder inside container
ADD . /src/

#add requirement dependencies to backend folder
ADD requirements.txt /src/

#set workdir
WORKDIR /src

#install libraries dependencies to container
RUN pip install -r requirements.txt
# && \
#    python -m pytest