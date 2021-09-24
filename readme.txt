React app was created following youtube tutorial:
  Fullstack Flask React Tutorial - Master Flask Basics and Build a Python Flask React App | 2020 HD

To set of the environment:
    yarn create react-app wallstreet_python_react
This command created the react app.

  mkdir api
Then, a folder called api/ was created for the flask backend.

  sudo apt install python3-virtualenv
virtualenv was downloaded.

  cd api
The directory was changed to the newly create api/ folder.

  virtualenv -p python3 venv
A virtual environment was created for the project.

  source ./venv/bin/activate
The virtual environment was activated.

  pip3 install Flask
Flask was installed.


To run the backend+frontend, open 2 terminals.
In The first terminal start the backend python file in api/
  python3 api.py

In the second terminal, start the react server
  yarn start

A proxy is used in package.json to connect port 5000 from the backend to port
3000 that the frontend runs on.


To build the project after downloading the repo:
From files I created, RedditScraper.py needs to import praw
  pip3 install praw

Interpreter.py needs to import yfinance
  pip3 install yfinance

Installed semantic-ui-react for the list component
  yarn add semantic-ui-react semantic-ui-css

Installed material-ui/core to get simple cards
  yarn add @material-ui/core


If praw is outdated, it updates often, run:
  pip install --upgrade praw


To run the project on bootup, cd into the api directory. Open 2 terminal windows
from this folder. In the first terminal run
  source ./venv/bin/activate
  python3 api.py

This activates the virtual environment and starts the backend server. Then, in
the other window
  source ./venv/bin/activate
  yarn start

This activates the virtual environment and starts the react server
  exit
Will close the virtual environment
