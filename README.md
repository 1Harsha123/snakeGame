# snakeGame

The provided program is a simple Python script that simulates a game between a user and a computer. The game involves three options: "snake," "gun," and "water." The program determines the winner based on the choices made by the user and the computer. Here's a brief logic breakdown of the program:

Import the random module to generate a random choice for the computer.
Define a function called check_winner that takes two parameters, computer and user, and determines the winner based on the choices.
Compare the choices of the computer and the user using a series of if-elif-else conditions:
If both choices are the same, return 0 (indicating a draw).
If the computer chooses "snake" and the user chooses "water," or if the computer chooses "water" and the user chooses "gun," or if the computer chooses "gun" and the user chooses "snake," return -1 (indicating the user's loss).
In all other cases, return 1 (indicating the user's win).
Define a list of options containing "snake," "gun," and "water."
Use the random.choice function to let the computer randomly select an option from the list.
Take user input for their choice and convert it to lowercase.
Call the check_winner function with the computer's choice and the user's choice, storing the result in the variable score.
Use the score variable to determine the outcome of the game:
If the score is 0, print "match is draw."
If the score is 1, print "you won."
If the score is -1, print "you lose."
Print the choices made by the user and the computer.
Overall, the program allows the user to play a simple game against the computer and provides the outcome based on the choices made.





