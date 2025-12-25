# Coffee Machine Simulator

A simple Python command-line program that simulates a coffee machine. Users can order drinks, insert coins, receive change, and view machine resources.

## Features

* Order **espresso**, **latte**, or **cappuccino**
* Checks for sufficient ingredients before making a drink
* Coin-based payment system (quarters, dimes, nickels, pennies)
* Calculates and returns change
* Tracks available resources and money
* Special commands for reporting status and shutting down

## How It Works

1. The user selects a drink.
2. The machine checks if enough resources are available.
3. The user inserts coins.
4. If payment is sufficient, the drink is made and change is returned.
5. Resources are updated accordingly.

## Commands

* `espresso`, `latte`, `cappuccino` — order a drink
* `report` — display current resources and money
* `off` — turn off the machine

## Requirements

* Python 3.x
* No external libraries required

## Running the Program

```bash
python main.py
```

## Purpose

This project was built to practice:

* Dictionaries and data structures
* Functions and control flow
* User input handling
* Basic simulation logic
