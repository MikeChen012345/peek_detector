# peek_detector

A python script to turn off the screen when you leave the computer or when someone is peeking your screen

## Installation

Run the following command to install the required packages

```pip install -r requirements.txt```

## Usage

Run the following command to start the script

```python peek_detector.py <-t --timeout><-q --q_quit><-h --help>```

## Options

`-h, --help` show this help message and exit

`-q, --q_quit` allow the user to press q to quit the program. Side effect: a small window will appear when the program is running.

`-t TIMEOUT, --timeout TIMEOUT` set the time to wait before turning off the screen

