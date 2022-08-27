# HangMan Python!

## About 

HangMan is a terminal game programed with Python, which runs in the Code Institute mock terminal on Heroku.

HangMan is a funny and a widely-known word game in which the goal is to guess the word.
It all depends on how good your vocabulary is and luck of your guesses to initially guess your words. 
[Read more about the game!](https://en.wikipedia.org/wiki/Hangman_(game))


Give it a try!

[Click here to try out the live game/project.](https://hangman-42.herokuapp.com/)



## User Experriense

![Responsive HangMan](assets/readmeimg/responsivepython.png)



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

![Board](assets/readmeimg/startgame.png)



- __In game Guess__

  - User input implemented 
  - View chosen guess
  

![Board](assets/readmeimg/gameguess.png)



- __In game Validation__

  - Only letters are verified as an input
  - The user can't guess the same letters twice
  - Letters outside the word size is not allowed
  - The Data is maintained in class instances
  

![Board](assets/readmeimg/gamevalidation.png)



### Features Left to Implement
In a near future, I would like to implement:
- 2 player mode




I decided to use two classes for the game model. One Board class and one Game class. 

- __Board Class__
  - self.size = To set the board size
  - self.num_ships = To set number of ships in-game
  - self.player = Bolian indicate if the board belongs to a player or computer
  - self.guesses = List of passed guesses
  - self.populate = Creates in-memory board with the players ship
  
  
- __Game Class__
  - self.size = To set the board size
  - self.num_ships = To set number of ships in-game
  - self.scores = Set score when ship is sunk



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


## Languages, Frameworks, IDE, Libraries and Programs

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
