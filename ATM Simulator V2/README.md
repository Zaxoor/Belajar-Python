# ATM Simulator V2

A simple command-line ATM simulator built with Python. This project allows users to manage their balance and track transactions through a menu-based interface.

## Features
- **Check Balance:** Display the current account balance.
- **Deposit Money:** Add money to the account with a minimum deposit requirement.
- **Withdraw Money:** Withdraw money while maintaining the minimum required balance.
- **Transaction History:** View a list of previous deposits and withdrawals.
- **Data Persistence:** Save the current balance and transaction history to a JSON file.
- **Input Validation:** Handle invalid numeric inputs and enforce transaction requirements.
- **Exit:** Close the program after saving the latest account data.

## Requirements
- Python 3.10 or later (or another compatible Python version).
- A code editor or terminal, such as Visual Studio Code.

## How to Run
1. Download or clone this project repository.
2. Make sure ATM_Simulator_V2.py and transactions.json are in the same folder. If the JSON file does not exist, the program will initialize the account with a default balance.
3. Open the project folder in Visual Studio Code or another code editor.
4. Open a terminal in the project folder.
5. Run the following command:
```bash
python ATM_Simulator_V2.py
```
6. Follow the on-screen menu and enter the appropriate option to use the available features.