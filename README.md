# 🃏 War Card Game (Python)

A card game built in python, using object oriented programming.

This python project uses classes, loops, lists and game logic while simulating a full game of War between two players.


## How the Game Works

The game starts off with **52 deck of cards**, which is shuffled before play begins.

- Each player gets even amount of cards. **26 cards**
- During each round:
    - Both players show the top card from their deck.
    - The player with the high ranking card than the other player wins the round.
    - The winner collects both cards and places them at the bottom of their deck.
- The game continues until one player has no cards remaining.

## WAR RULES

If both of the players deal their cards and both are the **same value**, it's a **WAR**.

DURING A WAR:

1. Each player places **three additional cards** face down.
2. The next card determines the winner.
3. The winning player collects **all cards** involved in the war.

If a player does not have enough cards to complete a war, they immediately lose the game

--

## Concepts practiced
- Object-Oriented Programming (OOP)
- Classes & Objects
- Constructors (`__init__`)
- Special Methods (`__str__`)
- Lists
- Loops
- Conditional Statements
- Methods
- Random Module
- Game Logic
- Data Structures

This project was created as a practice exercise for learning Python and object-oriented programming. It demonstrates how multiple classes can work together to model a real-world card game while reinforcing core programming concepts.
