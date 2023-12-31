# Proyect Model Wine:

This is a Repository for Wine Model Clasiffication proyect.

# Data set description:

This data set is related to the red variants of the Portuguese wine "Vinho Verde". The data set describes the amount of various chemicals present in wine and their effect on its quality.

![Texto alternativo](https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/Captura-de-pantalla-2021-05-08-a-las-23.27.15.png)

## Problem context:

Dishonest manufacturers have learned to dispense a mixture of water, sugar, aniline dye and citric acid from grape wine. It is very difficult to recognize a fake, not unique suitable verification methods. I will tell you how to determine the quality of wine in accessible ways.

When choosing wine in a store, we evaluate only the appearance of the bottle, which does not always save us from counterfeiting. Now you can fake a bottle and a label of a wine company even in the basement. The similarity with the original will be one hundred percent. when this value is selected, the quality of the wine is excluded due to appearance. The wine must be tasted before serving.

The quality of wine is its normative indicator for chemical composition, color, saturation, aroma and taste.

![Texto alternativo](https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/DvEs.gif)


## Overall analysis and results

The problem that is addressed is to predict the quality of the wine using the data provided. Knowing that there are many wines of normal, excellent and bad quality. And the solution (notebook) it can find in the next link: https://github.com/diegomendozaglez/proyectofinalwine/blob/main/notebook/NotebookWine1.ipynb

## Setup

### For Linux users:

* Change the directory to the `module-3/session-11/itesm_mlops/itesm_mlops` folder.
* Create a virtual environment with Python 3+:
  ```bash
  python310 -m venv venv
  ```
* Activate the virtual environment
  ```bash
  source venv/bin/activate
  ```
* Install the other libraries
  Run the following command to install the libraries/packages.
  ```bash
  py -m pip install -r ./mlops-winemodel/winemodel/requirements_dev.txt
  ```

### For Windows users:

* Change the directory to the `/mlops-winemodel` folder.
* Create a virtual environment with Python 3+:

  ```bash
  py -3.10 -m venv venv
  ```
* Activate the virtual environment using PowerShell

  ```bash
  venv\Scripts\Activate.ps1
  ```
* Install the other libraries
  Run the following command to install the libraries/packages.

  ```bash
  pip install -r ./mlops-mobilepc/winemodel/requirements_dev.txt
  ```

  > **NOTE**
  > Deactivate the virtual environment using this command at the end of its example.
  > Linux: ``bash deactivate`` Windows: `deactivate`
  >

## Pytest (Unit test)

Steps:

### Virtual environment

Activate the virtual environment with `Python 3.10`

For Linux:

```
venv\Scripts\Activate.ps1
```

For Windows:

```
venv\Scripts\Activate.ps1
```

> **NOTE**
> Deactivate the virtual environment using this command at the end of its example.
> Linux: ``bash deactivate`` Windows: `deactivate`

### Running the tests

The following test validates the [load_data.py](mobilepc/tests/test_mobilepc.py) module:

Follow the next steps to run the test.

* Change the directory and run the following command:
  ```bash
  cd /winemodel
  ```
* Then run:
  ```bash
  pytest ./tests/test_winemodel.py -v
  ```
* You should see the following data output:
  ```

  ====================================================================================================== test session starts ======================================================================================================
  platform win32 -- Python 3.10.9, pytest-7.4.0, pluggy-0.13.1 -- C:\Users\IOR_C\OneDrive\Documentos\GitHub\mlops-winemodel\venv\Scripts\python.exe
  cachedir: .pytest_cache
  rootdir: C:\Users\IOR_C\OneDrive\Documentos\GitHub\mlops-winemodel\winemodel
  plugins: anyio-3.7.1
  collected 4 items

  tests/test_mobilepc.py::test_outlierfix_transform PASSED                                                                                                                                                                   [ 25%] 
  tests/test_mobilepc.py::test_custom_value_fixed_transform PASSED                                                                                                                                                           [ 50%] 
  tests/test_mobilepc.py::test_csv_file_existence PASSED                                                                                                                                                                     [ 75%] 
  tests/test_mobilepc.py::test_pkl_file_existence PASSED                                                                                                                                                                     [100%] 

  ======================================================================================================= 4 passed in 0.96s ======================================================================================================= 
  ```

## Usage

### Individual Fastapi and Use Deployment

Run the next command to start the Wine Queality API locally:

> Remember to change up you directory to `mlops-winemodel/winemodel/winemodel`

```bash
uvicorn api.main:app --reload
```

#### Checking endpoints

1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Wine model Random Forest C. is all ready!"`
2. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:


![Texto alternativo](https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/Fast_api.png)



https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/Fast_api.png


### Running predictions

Try running the following predictions with the endpoint by writing the following values:

* **Prediction 1**Request

  ```bash
  {
   "fixed_acidity": 925.0,
   "volatile_acidity": 3.0,
   "clock_speed": 2.0,
   "citric_acid": 5.0,
   "residual_sugar": 0.0,
   "chlorides": 2.0,
   "free_sulfur_dioxide": 7.0,
   "total_sulfur_dioxide": 0.8,
   "density": 214.0,
   "pH": 9.0,
   "sulphates": 14.0,
   "alcohol": 367.0
  }
  ```

  Response body
  The output will be:

  ```bash
  "Predicted Quality: [2]"
  ```
* **Prediction 2**
  Request 

  ```bash
  {
   "fixed_acidity": 234.0,
   "volatile_acidity": 5.0,
   "clock_speed": 8.0,
   "citric_acid": 6.0,
   "residual_sugar": 1.0,
   "chlorides": 3.0,
   "free_sulfur_dioxide": 6.0,
   "total_sulfur_dioxide": 0.9,
   "density": 158.0,
   "pH": 8.0,
   "sulphates": 10.0,
   "alcohol": 322.0
  }
  ```

  Response 
  The output will be:

  ```
  "Predicted Quality: [1]"
  ```

### Training model

### Individual deployment of the API with Docker and usage

  ```
* Inspect the image created by running this command:

  ```bash
  docker images
  ```

  Output:

  ```bash
  REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
  winemodel-image           latest    0r8ti6231ac4   45 seconds ago   608MB
  ```

#### Run Mobile PC REST API

1. Run the next command to start the `winemodel-image` image in a container.

   ```bash
   docker run -d --rm --name winemodel-c -p 8000:8000 winemodel-image
   ```
2. Check the container running.

   ```bash
   docker ps -a
   ```

   Output:

   ```bash
   CONTAINER ID   IMAGE             COMMAND                   CREATED               STATUS               PORTS                     NAMES
   6e2f57198385   winemodel-image   "uvicorn main:app --…"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp   winemodel-c
   ```

#### Checking endpoints for app

1. Access `http://127.0.0.1:8000/`, and you will see a message like this `"Random Forest Classificator is all ready!"`
2. A file called `main_api.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:

![Texto alternativo](https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/FastApi2.PNG)

4. Try running the following predictions with the endpoint by writing the following values:

* **Prediction 1**Request body

  ```bash
  {
   "fixed_acidity": 925.0,
   "volatile_acidity": 3.0,
   "clock_speed": 2.0,
   "citric_acid": 5.0,
   "residual_sugar": 0.0,
   "chlorides": 2.0,
   "free_sulfur_dioxide": 7.0,
   "total_sulfur_dioxide": 0.8,
   "density": 214.0,
   "pH": 9.0,
   "sulphates": 14.0,
   "alcohol": 367.0
  }
  ```

  Response body
  The output will be:

  ```bash
  "Predicted Price Range: [2]"
  ```
* **Prediction 2**
  Request body

  ```bash
  {
   "fixed_acidity": 234.0,
   "volatile_acidity": 5.0,
   "clock_speed": 8.0,
   "citric_acid": 6.0,
   "residual_sugar": 1.0,
   "chlorides": 3.0,
   "free_sulfur_dioxide": 6.0,
   "total_sulfur_dioxide": 0.9,
   "density": 158.0,
   "pH": 8.0,
   "sulphates": 10.0,
   "alcohol": 322.0
  }
  ```

  Response body
  The output will be:

  ```
  "Predicted Price Range: [1]"
  ```

#### Opening the logs

1. Run the command

   ```bash
   docker exec -it mobilepc-c bash
   ```

   Output:

   ```bash
   root@44298942e775:/#
   ```
2. Check the existing files:

   ```bash
   ls
   ```

   Output:

   ```bash
   Dockerfile  __init__.py  bin   data  etc   lib    lib64   main.py       media  modelwine.py         models     opt        preprocess  requirements.txt  run   srv  tmp    usr
   README.md   __pycache__  boot  dev   home  lib32  libx32  main_api.log  mnt    modelwine_train.log  models_ml  predictor  proc        root              sbin  sys  train  var
   ```
3. Open the file `main_api.log` and inspect the logs with this command:

   ```bash
   vim main_api.log
   ```

   Output:

   ```log
   2023-08-24 02:22:17,527:main:main:INFO:Random Forest Classificator Classifier is all ready!
   2023-08-24 02:23:47,835:main:main:INFO:Predicted result: [2]
   2023-08-24 02:23:40,973:main:main:INFO:Succesfully runned: {'message': 'Model training script executed successfully', 'response_text': 'test precision: 0.84231940\ntest accuracy: 0.9525\nModel saved in models_ml/random_forest.pkl\n'}
   2023-08-24 02:24:54,624:main:main:INFO:Predicted result: [2]
   2023-08-24 02:25:08,842:main:main:INFO:Predicted result: [2]

   ```
4. Copy the logs to the root folder:

   ```bash
   docker cp modelwine-c:/main_api.log .
   ```

   Output:

   ```bash
   Successfully copied 2.05kB to ...\mlops-modelwine\.
   ```

#### Delete container and image

* Stop the container:

  ```bash
  docker stop modelwine-c
  ```
* Verify it was deleted

  ```bash
  docker ps -a
  ```

  Output:

  ```bash
  CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
  ```
* Delete the image

  ```bash
  docker rmi modelwine-image
  ```

  Output:

  ```bash
  Deleted: sha256:25b69b866983c9f8ad67f32ae0c254e9730adfa1c7c114fb9e484a0190ad1473
  ```

### Complete deployment of all containers with Docker Compose and usage

#### Create the network

First, create the network AIService by running this command:

```bash
docker network create AIservice
```

#### Run Docker Compose

* Ensure you are in the directory where the docker-compose.yml file is located
* Run the next command to start the App and Frontend APIs

  ```bash
  docker-compose -f mobilepc/mobilepc/docker-compose.yml up --build
  ```

  You will see something like this:

  ```bash
   ✔ Container mobilepc-app-1       Created                                                                                                                                                                           0.2s 
   ✔ Container mobilepc-frontend-1  Created                                                                                                                                                                           0.0s 
  Attaching to mobilepc-app-1, mobilepc-frontend-1
  modelwine-app-1       | INFO:     Will watch for changes in these directories: ['/']
  modelwine-app-1       | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
  modelwine-app-1       | INFO:     Started reloader process [1] using StatReload
  modelwine-frontend-1  | INFO:     Will watch for changes in these directories: ['/']
  modelwine-frontend-1  | INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
  modelwine-frontend-1  | INFO:     Started reloader process [1] using StatReload
  modelwine-app-1       | INFO:     Started server process [7]
  modelwine-app-1       | INFO:     Waiting for application startup.
  modelwine-app-1       | INFO:     Application startup complete.
  modelwine-frontend-1  | INFO:     Started server process [8]
  modelwine-frontend-1  | INFO:     Waiting for application startup.
  modelwine-frontend-1  | INFO:     Application startup complete.
  ```

#### Checking endpoints in Frontend

1. Access `http://127.0.0.1:3000/`, and you will see a message like this `"Front-end is all ready to go!"`
2. A file called `frontend.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:3000/docs`, the browser will display something like this:

![Texto alternativo](https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/MM.png)

4. Try running the following predictions with the endpoint by writing the following values:

* **Prediction 1**Request

  ```bash
  {
   "fixed_acidity": 925.0,
   "volatile_acidity": 3.0,
   "clock_speed": 2.0,
   "citric_acid": 5.0,
   "residual_sugar": 0.0,
   "chlorides": 2.0,
   "free_sulfur_dioxide": 7.0,
   "total_sulfur_dioxide": 0.8,
   "density": 214.0,
   "pH": 9.0,
   "sulphates": 14.0,
   "alcohol": 367.0
  }
  ```

  Response
  The output will be:

  ```bash
  "Predicted Price Range: [2]"
  ```
* **Prediction 2**
  Request

  ```bash
  {
   "fixed_acidity": 234.0,
   "volatile_acidity": 5.0,
   "clock_speed": 8.0,
   "citric_acid": 6.0,
   "residual_sugar": 1.0,
   "chlorides": 3.0,
   "free_sulfur_dioxide": 6.0,
   "total_sulfur_dioxide": 0.9,
   "density": 158.0,
   "pH": 8.0,
   "sulphates": 10.0,
   "alcohol": 322.0
  }
  ```

  Response body
  The output will be:

  ```
  "Predicted Wine Quality: [1]"
  ```

#### Opening the logs in Frontend

Open a new terminal, and execute the following commands:

1. Copy the `frontend` logs to the root folder:

   ```bash
   docker cp modelwine-frontend-1:/frontend.log .
   ```

   Output:

   ```bash
   Successfully copied 2.56kB to ...\mlops-modelwine\.
   ```
2. You can inspect the logs and see something similar to this:

   ```bash
   INFO: 2023-08-23 05:02:57,993|main|Front-end is all ready to go!
   DEBUG: 2023-08-23 05:04:30,195|main|Incoming input in the front end: {'fixed_acidity': 925.0, 'volatile_acidity': 3.0, 'clock_speed': 2.0, 'citric_acid': 5.0, 'residual_sugar': 0.0, 'chlorides': 2.0, 'free_sulfur_dioxide': 7.0, 'total_sulfur_dioxide': 0.8, 'density': 214.0, 'pH': 9.0, 'sulphates': 14.0,'alcohol': 367.0}
   DEBUG: 2023-08-24 03:25:32,894|main|Prediction: "Predicted Wine Quality: [2]"
   INFO: 2023-08-24 03:25:45,166|main|Checking health: "Wine Random Forest classifier is all ready!"
   INFO: 2023-08-24 03:25:48,428|main|Checking health: "Wine Random Forest classifier is all ready!"
   INFO: 2023-08-24 03:25:51,815|main|Checking health: "Wine Random Forest classifier is all ready!"
   ```

#### Opening the logs in App

Open a new terminal, and execute the following commands:

1. Copy the `app` logs to the root folder:

   ```bash
   docker cp modelwine-app-1:/main_api.log .
   ```

   Output:

   ```bash
   Successfully copied 2.56kB to .../itesm-mlops-project/.
   ```
2. You can inspect the logs and see something similar to this:

   ```bash
   2023-08-24 03:26:40,891:main:main:INFO:Predicted result: [2]
   2023-08-24 03:26:46,161:main:main:INFO:Random Forest Classifier is all ready!
   2023-08-24 03:26:47,425:main:main:INFO:Random Forest Classifier is all ready to go!
   2023-08-24 03:26:48,813:main:main:INFO:Random Forest Classifier is all ready to go!
   ```

### Delete the containers with Docker Compose

1. Stop the containers that have previously been launched with `docker-compose up`.

   ```bash
   docker-compose -f modelwine/modelwine/docker-compose.yml stop 
   ```

   Output:

   ```bash
   [+] Stopping 2/2
    ✔ Container modelwine-frontend-1  Stopped   
    ✔ Container modelwine-app-1       Stopped 
   ```
2. Delete the containers stopped from the stage.

   ```bash
   docker-compose -f proyectofinalwine/winequality_model/docker-compose.yml rm
   ```

   Output:

   ```bash
   ? Going to remove mobilepc-frontend-1, mobilepc-app-1 Yes
   [+] Removing 2/0
    ✔ Container modelwine-frontend-1  Removed   
    ✔ Container modelwine-app-1       Removed   
   ```
3. Delete the image

   ```bash
   docker rmi modelwine-frontend
   docker rmi modelwine-app
   ```

   Output:

```bash
Untagged: modelwine-frontend:latest
Deleted: sha256:cad7ed656a014cb6656ad8749b203ea216be903cc4e051af3cdc3997b7ecf2c0

Untagged: modelwine-app:latest
Deleted: sha256:fa054a5b48a475eb0589950d42d5323b4e43607f89e4b006bbd1a33e472e364b
```

## Pre-commits

In attempt to assure quality across all modules, this proyect has a pass throug phase using Pre-commits.

Pre-commits are automated checks that run on your code before you commit changes, helping ensure code quality and consistency.

### Prerequisites

1. Python is installed on your system.
2. Visual Studio Code (VSC) is installed on your system.
3. `pip` is installed on your system.

### Step 1: Install `pre-commit`

First, you need to install the `pre-commit` tool on your system. Open your terminal or command prompt and run the following command:

```bash
pip install pre-commit
```

### Step 2: Create a Pre-Commit Configuration File

Create a file named `.pre-commit-config.yaml` in the root of your Python project. This file will define the pre-commit hooks to be executed.

### Step 3: Configure Pre-Commit Hooks

In the  [pre-commit file](.pre-commit-config.yaml), we have defined the pre-commit hooks you want to run. Each hook represents a specific check on the code. There are many pre-configured hooks available, and you can also create custom hooks if needed.

### Step 4: Initialize Pre-Commit for Your Project

After looking the `.pre-commit-config.yaml` file, initialize pre-commit for this project. Open your terminal or command prompt, navigate to the root directory of this project, and run the following command:

```bash
pre-commit install
```

Output

```bash
pre-commit installed at .git/hooks/pre-commit
```

> **NOTE**
> If you want to see the default hidden folder `.git`, follow the steps in this link: https://linuxpip.org/vscode-show-hidden-files/

### Step 5: Commit Your Changes

With the pre-commit hooks installed, you can now make changes to the Python code. When you're ready to commit changes, run the following command to trigger the pre-commit checks:

```bash
git commit -m "add pre-commit file"
```

Output

`<summary>`Pre-commit output, click to collapse `</summary>`

    ``bash     [WARNING] The 'rev' field of repo 'https://github.com/pre-commit/mirrors-autopep8' appears to be a mutable reference (moving tag / branch).  Mutable references are never updated after first install and are not supported.  See https://pre-commit.com/#using-the-latest-version-for-a-repository for more details.  Hint: `pre-commit autoupdate` often fixes this.     [INFO] Initializing environment for https://github.com/pre-commit/mirrors-autopep8.     [INFO] Initializing environment for https://github.com/PyCQA/flake8.     [INFO] Installing environment for https://github.com/pre-commit/mirrors-autopep8.     [INFO] Once installed this environment will be reused.     [INFO] This may take a few minutes...     [INFO] Installing environment for https://github.com/PyCQA/flake8.     [INFO] Once installed this environment will be reused.     [INFO] This may take a few minutes...     autopep8.............................................(no files to check)Skipped     flake8...............................................(no files to check)Skipped     [main 210cf52] add pre-commit file     3 files changed, 77 insertions(+)     create mode 100644 .pre-commit-config.yaml     create mode 100644 module-2/session-5/README.md     ``

Pre-commit will run all the defined hooks on the files you've staged for the commit. If any issues are found (e.g., trailing whitespace, linting errors, etc.), the commit will be halted, and you'll need to address the problems before you can successfully commit.

## Resources

Here you will find information about this project and more.

### Information sources

There is a total of 273 notebooks already developed in relation to this dataset, attached the link of the top 3 of the most voted:

https://www.kaggle.com/code/georgyzubkov/wine-quality-exploratory-data-analysis-ml https://www.kaggle.com/code/jcaliz/ps-s03e05-a-complete-eda https://www.kaggle.com/code/qusaybtoush1990/wine-quality

![Texto alternativo](https://github.com/diegomendozaglez/proyectofinalwine/blob/main/imagenes/Captura.PNG)

## Contact information

  * **Development Lead**

    * Diego Alejandro Mendoza González, Correo TEC: <a01688735@tec.mx>
    * [LinkedIn](https://www.linkedin.com/in/diego-mendoza-4348101a3/)
