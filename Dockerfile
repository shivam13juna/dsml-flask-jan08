FROM python:3.8-slim-buster

# Set the working directory to /app

WORKDIR /flask-loan-app 
# this is the directory inside the container


RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
# copy ../../flsk-folder/ .
# Copy everything from the current directory to the PWD (Present Working Directory) inside the container

# CMD [ "python3", "flask", "run", "--host=0.0.0.0"] 


# python3 flask --app app.py run
CMD ["python", "-m","flask", "--app", "app.py", "run", "--host=0.0.0.0"]

#  python3 -m flask run --host=0.0.0.0
# here host can be any ip address


# if I have a bash file then I can use RUN chmod +x filename.sh


# 1