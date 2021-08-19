from prompt_toolkit import PromptSession
from utils import marvin_says
from responses import handle_response

if __name__ == '__main__':
    session = PromptSession()
    marvin_says("Oh, it's you.")

    while True:
        try:
            text = session.prompt('> ')
        except KeyboardInterrupt:
            marvin_says("Changed your mind did you? Typical.")
        except EOFError:
            break
        else:
            handle_response(session, text)

    marvin_says("Yes, well, I'd had enough of you as well")
