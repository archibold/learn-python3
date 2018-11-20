## My source of new cool toy: Python3

I have decided to learn a new language and that is Python3.
Here I'll push some code with description what it is and how to use it

## notify.py
Because I want to use technology to solve a problems and I am looking for a new flat in a different city so I wrote a notifier.
It download the page from olx service (which has a filters already in query) and notify me every 30 min if somebody add new advertisement.

I use to this ntfy
```
pip3 install dbus-python
pip3 install ntfy
```
everything is saved in `flats.json` file

to run it:
```
python3 notify.py
```

it is never ending loop so if you want to quit you have to use `Ctrl+C` in terminal
