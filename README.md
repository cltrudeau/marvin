# Marvin Chat Bot: A Cucumber / Behave Demo

Marvin is a very simple chat bot that you can converse with on the command
line. The bot's responses are based on [Marvin the Paranoid
Android](https://en.wikipedia.org/wiki/Marvin_the_Paranoid_Android) from the
[Hitchhiker's Guide to the
Galaxy](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy)
series. You're welcome to have fun chatting with Marvin, but his primary
purpose is to show off the Behavioural Driven Development (BDD) tool,
[Cucumber](https://cucumber.io/). 

There are several ways of doing Cucumber in Python, one of the most popular is
the [https://behave.readthedocs.io/en/stable/index.html](Behave) toolkit.
Behave uses decorators to match Cucumber steps to Scenarios and feature files.
This demo also has a testing script that calls Behave, calculates code
[`coverage`](https://coverage.readthedocs.io), and then runs
[`pyflakes`](https://pypi.org/project/pyflakes/)

To chat with marvin:

```
$ python marvin.py
```

You can exit your conversation by typing "goodbye" or hitting CTRL-D.

To see the BDD tests in action you will need some libraries installed:

```
$ python -m pip install -r requirements.txt
```

Once installed, the `behave` command to execute all the tests, or run the
`runtests.sh` script to execute `behave`, calculate the `coverage`, and
analyze the code with `pyflakes`.

## Inspiration

This project was based on an [idea by Daniel Lynn](https://github.com/technicallyagile/marvin_devops_eclipse), originally developed in Java and Eclipse.
