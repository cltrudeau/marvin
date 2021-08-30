#! /usr/bin/env python
#
# marvin.py
#
# Overly simple chat bot to demonstrate Cucumber and Python Behave
#
# $ python marvin.py
#
# ===========================================================================

__version__ = '0.1'

import random, re
import enum        # unused import to demo pyflakes

# ===========================================================================
# Response Data
# ===========================================================================

RESPONSES = {
    'life': "Life. Don't talk to me about life.",
    'feel': "I think you ought to know I'm feeling depressed",
    'marvin': "It gives me a headache just trying to think down to your level.",
    'happy': "This will all end in tears, I just know it.",
    'alien': "I brought the aliens. Don't thank me or anything.",
    'today':"I could calculate your chances of survival, but you wouldn't like it.",
    'angry':"Life. Loathe it or ignore it, you can't like it.",
    'know':"I know. Wretched, isn't it?",
    'question':"It won't work, I have an exceptionally large mind.",
    'answer':"I have a million ideas. They all point to certain death.",
    'sad':"My capacity for happiness, you could fit into a matchbox without taking out the matches first.",
    'hello':"The first ten million years were the worst, and the second ten million years, they were the worst too. The third ten million years I didn't enjoy at all. After that I went into a bit of a decline",
}

RESPONSE_KEYS = list(RESPONSES.keys())

REPEAT = "You're repeating yourself. Think I wouldn't notice?"

match_word = re.compile(r"(\w+)")

# ===========================================================================

def marvin_says(message):
    print(f'🤖 says: {message}')

# ---------------------------------------------------------------------------

def handle_response(history, text):
    global RESPONSES, REPEAT

    if text in history:
        marvin_says(REPEAT)
        return

    for word in match_word.findall(text):
        word = word.lower()
        alternate = word
        if word.endswith('s'):
            alternate = word[:-1]

        if word in RESPONSES:
            marvin_says(RESPONSES[word])
            return
        elif alternate in RESPONSES:
            marvin_says(RESPONSES[alternate])
            return

    # No word match, pick something random
    word = random.choice(RESPONSE_KEYS)
    marvin_says(RESPONSES[word])

# ===========================================================================

if __name__ == '__main__':
    history = []
    marvin_says("Oh, it's you.")

    while True:
        try:
            text = input('> ')

            if text.lower() in ['goodbye', 'exit', 'quit']:
                break
        except KeyboardInterrupt:
            marvin_says("Changed your mind did you? Typical.")
        except EOFError:
            break
        else:
            handle_response(history, text)
            history.append(text)

    marvin_says("Yes, well, I'd had enough of you as well")
