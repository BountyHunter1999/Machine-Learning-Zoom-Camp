# Description of the problem
## Data Description
This dataset was created by combining different datasets already available independently but not combined before. In this dataset, 5 heart datasets are combined over 11 common features which makes it the largest heart disease dataset available so far for reasearch purposes. The five datasets used for its curation are:

- Cleveland: 303 observations
- Hungarian: 294 observations
- Switzerland: 123 observations
- Long Beach VA: 200 observations
- Stalog (Heart) Data Set: 270 observations
=> Total: 1190 observations Duplicated: 272 observations

Final dataset: 918 observations

##  Attribute Information
- Age: age of the patient [years]
- Sex: sex of the patient [M: Male, F: Female]
- ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
- RestingBP: resting blood pressure [mm Hg]
- Cholesterol: serum cholesterol [mm/dl]
- FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
- RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
- MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
- ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
- Oldpeak: oldpeak = ST [Numeric value measured in depression]
- ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
- HeartDisease: output class [1: heart disease, 0: Normal]

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


# For the cloud(on heroku) 
# SITE LINK: https://ml-zoomcamp-cap-docker.herokuapp.com/
# Send POST request to https://ml-zoomcamp-cap-docker.herokuapp.com/predict


- install heroku with `curl https://cli-assets.heroku.com/install.sh | sh`

## HOW I PUSHED THE IMAGE IN HEROKU:

Push docker image to Heroku container registry. When you run the below command, the Dockerfile will be used to build the docker image locally on your machine and then push the image to Heroku container registry. Using the `-a` flag you specify the application name (e.g. `ml-zoomcamp-cap-2-docker` app that you created above).

1. firstly, installed heroku and login to your heroku account using `heroku login`
2. `heroku container:login`
3. `heroku create ml-zoomcamp-cap-2-docker`
4. `heroku container:push web -a ml-zoomcamp-cap-2-docker`

### Release the container

- **Release container**: Deploy container on Heroku. When you run the below command, a docker container will be launched in Heroku from the docker image that you pushed to Heroku container registry.
    - `heroku container:release web -a ml-zoomcamp-cap-2-docker`

- one thing to note is that when releasing the image in heroku won't work cause we're custom binding our port in our image layer but heroku doesn't allow that so we must do a certain tweak for it to work

```docker
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
```

```docker
ENTRYPOINT ["gunicorn", "predict:app"]
```