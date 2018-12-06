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

## 25min.py
This application is about 25min work and 5 min break during your office work
It uses `ntfy` to notify you every 30mm that it's time for a break

```
pip3 install dbus-python
pip3 install ntfy
```

to run it:
```
python3 25min.py
```

## kodpocztowy.py
this app is useful only for polish people who is looking for a zip code from city and street

How to use is
```
pip3 install BeautifulSoup
```

to run it
```
python3 kodpocztowy.py "city" "street"
```
