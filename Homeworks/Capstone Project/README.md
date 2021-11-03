# Description of the problem

- This dataset contains about 10 years of daily weather observations from many locations across Australia.
- RainTomorrow is the target variable to predict. It means -- did it rain the next day, Yes or No? This column is Yes if the rain for that day was 1mm or more.
- Our Goal is to design a predictive model with the use of machine learning algorithms to forecast whether or not it will rain tomorrow in Australia.

# Instructions on how to run the project
=> remember to use the see the Dockerfile

## Creating the environment

- get pipenv: `pip install pipenv`
- create a new virtual environment and enter into it: `pipenv shell`

## Package installation:

- `pipenv install flask gunicorn scikit-learn==0.24.1 pandas numpy`

or, for installation from the `pipfile` 

⇒ if U have my piplock file then u can just do `pipenv install` to install the required packages

## Building the docker file

- After creating the `Dockerfile`, run this command to build the docker image `docker build -t capstone .`

## Run the docker image

- `docker run -it -p 9696:9696 --rm capstone:latest`

## Run the project

### Local Machine:

- once the container is running we can do a post request to the endpoint (on ur local machine)

`"http://localhost:9696/predict"`

- Now, u can run `python predict_test.py` to see the result, u can tinker with the data there to view the results
- As the `Humidity3pm` is a major factor that influence our model output u can see the changes it will have in our model

# For the cloud(on heroku) 
# SITE LINK: https://ml-zoomcamp-cap-docker.herokuapp.com/
# Send POST request to https://ml-zoomcamp-cap-docker.herokuapp.com/predict


- install heroku with `curl https://cli-assets.heroku.com/install.sh | sh`

## HOW I PUSHED THE IMAGE IN HEROKU:

Push docker image to Heroku container registry. When you run the below command, the Dockerfile will be used to build the docker image locally on your machine and then push the image to Heroku container registry. Using the `-a` flag you specify the application name (e.g. `ml-zoomcamp-cap-docker` app that you created above).

1. firstly, installed heroku
2. `heroku container:login`
3. `heroku create ml-zoomcamp-cap-docker`
4. `heroku container:push web -a ml-zoomcamp-cap-docker`

### Release the container

- **Release container**: Deploy container on Heroku. When you run the below command, a docker container will be launched in Heroku from the docker image that you pushed to Heroku container registry.
    - `heroku container:release web -a ml-zoomcamp-cap-docker`

- one thing to note is that when releasing the image in heroku won't work cause we're custom binding our port in our image layer but heroku doesn't allow that so we must do a certain tweak for it to work

```docker
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
```

```docker
ENTRYPOINT ["gunicorn", "predict:app"]
```