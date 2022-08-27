# HangMan Python!
## Project Overview

The Economics Data Analysis Tool is a terminal based application that allows for data calculation and plotting using Google Sheets. This has been created as part of my Project 3 for Code Institute.

## Table of Contents

1. [User Experience (UX)](#ux)
    * [Strategy](#strategy)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Design](#design)
    * [Skeleton](#skeleton)
        * [Flowchart](#flowchart)
2. [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
3. [Technologies Used](#tech-used)
4. [Testing](#testing)
    * [User Stories Testing](#user-testing)
    * [Validation Testing](#validation-testing)
    * [Known Issues and Resolutions](#issues)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

## User Experience (UX) <a name="ux"></a>

## Strategy <a name="strategy"></a>

### Project Goals <a name="project-goals"></a>

The main goal for the Economics Data Analysis Tool is to provide a terminal-based application which allows the user to import data from Google Sheets, and complete various calculations with the scope for plotting the data as the end result.

The main target audience for this application is a fictional economist who is interested in analysing various economic data for the UK over the past 10 years. The application would allow for such analysis by completing various calculations and exporting this data back to Google Sheets, as well as allowing the economist to plot data based on their selection. 

### User Stories <a name="user-stories"></a>

* __Site User Goals:__

    * I want to import data from Google Sheets.
    * I want to calculate the total sum for each column of data and update the worksheet.
    * I want to calculate the average for each column of data and update the worksheet.
    * I want to calculate the estimate for each column of data for the next year and update the worksheet.
    * I want to plot the data across all available 'Years' for the selected column inclusive of the estimate data and choose the plot type.
    * I want to view the underlying data for the plotted output.

* __Site Owner Goals:__

    * I want to provide an application which allows user to import data from Google Sheets.
    * I want to provide an application which allows for data calculation for imported data (sum, average, estimate).
    * I want to provide an application which allows user to plot data based on their selection.
    * I want to provide an application which allows user to view the data selected for the plotting.


## Scope <a name="scope"></a>

To achieve the strategy goals, I want to implement the following features:

* A function which will import the data from Google Sheets.
* A function which will calculate the total sum and update the worksheet.
* A function which will calculate the average and update the worksheet.
* A function which will calculate the estimate for next year and update the worksheet.
* A function which will allow the user to select column to plot data for y-axis.
* A function which will allow user to select the plot type from the listed options.
* A function which will plot data based on the selection and confirm to the user that this has been plotted, in addition displaying the data selected for the plot on the terminal.

## Design <a name="design"></a>

As this is terminal based application, the design is kept as the basic terminal colours and fonts as per the template used for the deployed project.

## Skeleton <a name="skeleton"></a>

### Flowchart <a name="flowchart"></a>

Due to the project being a terminal-based application, no wireframes were created for this. Instead, a flowchart has been created to display the application process.

Flowchart was created using [diagrams.net](https://www.diagrams.net/).

![](https://github.com/Tinks18/Python-Hangman/blob/main/assets/images/flowchart.png)

## About 

HangMan is a terminal game programed with Python, which runs in the Code Institute mock terminal on Heroku.

HangMan is a funny and a widely-known word game in which the goal is to guess the word.
It all depends on how good your vocabulary is and luck of your guesses to initially guess your words. 
[Read more about the game!](https://en.wikipedia.org/wiki/Hangman_(game))


Give it a try!

[Click here to try out the live game/project.](https://hangman-42.herokuapp.com/)



## User Experriense

![Responsive HangMan](https://github.com/Tinks18/Python-Hangman/blob/main/assets/images/hangman-min.png)



## How to play

In this version of HangMan the user starts the game by first typing Y if they would like to play on.
By typing in the Y , the game will then fire on and the user will have the ability to guess their first word
by guessing and calling out coordinates to find out the computer ships and sink them.
The game will randomly generate and populate underscores corresponding to the number of letters in the word.
The game will always start on: 0 row and 0 columns.
Guesses are marked on the terminal with the correct guess being displayed instead of the underscore.
To gain a win, you have to guess all the letters to the word before you run out of turns!



## Features 

### Existing Features

- __Start the Game__

  - One underscore each are generated on the specified word size
  - Words are randomly displayed on the termnal
  - The player can see where the letters are located by the word displayed instead of underscore 
  - For wrong guesses the computer displays an error
  - For letters already guessed the computer displays an error
  - If the player wins if the correct word is input before running out of tries
  - The player can not see the correct word as required by the computer  

![Board](https://github.com/Tinks18/Python-Hangman/blob/main/assets/images/hangman-start-min.png)



- __In game Guess__

  - User input implemented 
  - View chosen guess
  

![Board](https://github.com/Tinks18/Python-Hangman/blob/main/assets/images/hangman-guess-min.png)



- __In game Validation__

  - Only letters are verified as an input
  - The user can't guess the same letters twice
  - Letters outside the word size is not allowed
  - The Data is maintained in class instances
  

![Board](https://github.com/Tinks18/Python-Hangman/blob/main/assets/images/validation-min.png)



### Features Left to Implement
In a near future, I would like to implement:
- google sheets to store data


## Testing 

- Code validator and test
  - [PEP 8 linter](http://pep8online.com/)
  - No errors were found when passing through the test.

- Manual invalid inputs
  - Validate that Value Error is given to the user when wrong value is inputted
  - Write string, text instead of numbers when numbers are expected
  - Out of bounds inputs example out of grid number
  - Same guess cannot be performed twice

- Local terminal and the Code institute Heroku terminal
  - Test done on my local terminal in Visual Studio IDE
  - Test done when project was deployed on Heroku with the Code Institute mockup terminal


### Bugs

No known bugs
  

- Validator Testing
  - PEP8
    - No errors were returned from (http://pep8online.com/checkresult)

## Technologies Used <a name="tech-used"></a>

For this project the main language used is __Python__.

I have also utilised the following frameworks, libraries, and tools:

* [Pandas](https://pandas.pydata.org/): 
    * Pandas Library has been used to allow for the creation of DataFrames and for plotting data.
* [Plotext](https://pypi.org/project/plotext/):
    * Plotext has been used to for plotting data in the terminal.
* [GitPod](https://www.gitpod.io/): 
    * I used GitPod as the IDE for this project and Git has been used for Version Control.
* [GitHub](https://www.github.com/): 
    * GitHub has been used to create a repository for the project and receive updated commits from GitPod.
* [Heroku](https://www.heroku.com/): 
    * Heroku has been used to create a repository to host the project and receive updated commits from GitPod.
* [gspread](https://pypi.org/project/gspread/): 
    * gspread has been used to access, update and manipulate data from Google Sheets.
* [Google Cloud Platform](https://cloud.google.com/): 
    * Google Cloud Platform has been used for APIs and credentials to be able to access Google Sheets with the relevant data.
* [World Bank Data](https://data.worldbank.org/): 
    * World Bank was used as a source of the data for the economic indicators used in this project.
* [PEP8 Online Validation Service](http://pep8online.com/): 
    * The PEP8 Online Validation Service was used to validate the Python document for this project and to identify any issues with the code.
* [StackOverflow](https://stackoverflow.com/): 
    * StackOverflow was used to assist with any troubleshooting issues during the course of the project.
* [diagrams.net](https://www.diagrams.net/):
    * diagrams.net was used to create the flowchart for this project.
* [Am I Responsive](http://ami.responsivedesign.is/):
    * Am I Responsive was used to create the header image for the README file.

[Python:](https://en.wikipedia.org/wiki/History_of_Python)
- The programming language Python was used. 

[Python random library:](https://docs.python.org/3/library/random.html)
- random.randint was used to generate random integer numbers in the game. 

[GitHub:](https://github.com/)
- GitHub was used to store the projects code after being pushed from Git.

[Visual Studio Code:](https://code.visualstudio.com/)
- Was used to develop and write my project locally.

[Gitpod:](https://www.gitpod.io/)
- Was used to complement the development and write my project and push all commits through integrated "git" to Github.

[Heroku:](https://www.heroku.com/what)
- Was used for deployment of the project live in the cloud.



## Deployment

This project was published and deplyed using the Code Institute mock teminal for Heroku
 - Steps for deployment: 
   - Fork or clone this repository
   - Create a new Heroku application
   - Set the buildpack in the setting to "heroku/python" and "heroku/nodejs"
   - In the "Deploy" menu chose "Deployment method" GitHub
   - Connect and choose the repository in the "App connected to GitHub" 
   - Choose either "Automatic deployment" = which means that every push to the branch you specify will deploy a new version of this app 
   - "Manual deploy" = this will deploy the current state/version of the branch   

The live link can be found here - https://HangMan-ms3.herokuapp.com/



## Cloning

If you wish to clone this repository you can use following steps:
 - Go to the Git Hub website and log in.
 - Locate the Repository used for this project.
 - Under the Repository name locate the button "Code" and once clicked you will see the options to get the url to the repository
   copy the URL based on the protocol that you would like to use. 
 - At the terminal type `git clone` and paste the url copied from the step above.



## Credits 

### Credits for the information and learning material i've used:

- (https://stackoverflow.com/)
- (https://docs.python.org/3/library/)
- (https://github.com/dmoisset/HangMan-dojo)
- Code Institute project 3 Scope video

### Acknowledgments

- My mentor Guido Cecilio for his support.
- Code Institute idea from Project Portfolio 3 (Example Idea Nr 2)
- Code Institute project 3 Scope video 









