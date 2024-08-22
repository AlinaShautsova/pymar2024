# *Homework29: Flask App*

*This is a Flask application designed to display a random cat GIF.*

## *Prerequisites*

* *Python 3.8 or higher*
* *Python package installer*
* *Docker*

### *Build the Docker image*

*Run the following command in your project directory to create the Docker 
image:*


docker build -t flask-app .


## *Running the Container*

*Execute the command below to run the Docker container and map the ports:*


docker run -p 8866:8866 flask-app


### *Access the Application*


*Visit http://localhost:8866 in your web browser to view the application.*


### *Structure of the project*
```
├── app.py               # Main Flask application file
├── Dockerfile           # Configuration of Docker file for image creation
├── requirements.txt     # File listing the Python dependencies
└── templates
    └── index.html       # The cat GIFs is displaying by HTML template
```

### *Stop and Remove the Container*


docker stop my-python-app
docker rm my-python-app
