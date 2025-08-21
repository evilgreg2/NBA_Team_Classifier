# NBA Teams Classifier

Given an image of  a player or basketball jersey, this model will attempt to classify the team.
The project currently correctly classifies images as either Chicago Bulls or Boston Celtics
I plan to add more teams in the future.




## The Algorithm

This application uses a retrained resnet18 model that is running using the Jetson Utils imagenet.


## Running this project
1. Clone this repository onto your Jetson Nano 
2. From the repository root run the python script `python3 NBA_Net.py <INPUT> <OUTPUT>`

After running this script it should load up the retrained imagenet and process the provided input which it will
classify as either Chicago Bulls or Boston Celtics.


[View a video demonstration here](https://www.youtube.com/watch?v=eOQji10Isis)



# Data Sources
* [2019 - 2020 NBA Player Images Dataset](https://www.kaggle.com/datasets/djjerrish/nba-player-image-dataset-201920)
* [2019 - 2020  NBA Player Roster Dataset](https://www.kaggle.com/datasets/nicklauskim/nba-per-game-stats-201920)
