from behave import given, when, then
from marvin.responses import handle_response

# ===========================================================================
# Mock prompt_toolkit PromptSession object

class History:
    def __init__(self, past_strings):
        self.past_strings = []

    def get_strings(self):
        return self.past_strings

class Session:
    def __init__(self, past_strings):
        self.history = History(past_strings)

# ===========================================================================

#Scenario: Repeated text
#    Given I have spoke to Marvin before
#    When I repeat myself
#    Then I should be told I'm repeating


@given('I have spoken to Marvin before')
def step(context):
    context.session = Session('repeating myself')

@when('I repeat myself')
def step(context):
    context.response = handle_response(context.session, 'repeating myself')

@then("I should be told I'm repeating")
def step(context):
    assert "You're repeating yourself" in context.reponse
