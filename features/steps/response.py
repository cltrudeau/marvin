from behave import given, when, then
from marvin import handle_response

# ===========================================================================

# --- Scenario: Repeated text

@given('I have spoken to Marvin before')
def step(context):
    context.history = ['repeating myself']


@when('I repeat myself')
def step(context):
    handle_response(context.history, 'repeating myself')


@then("I should be told I'm repeating")
def step(context):
    assert "You're repeating yourself" in context.stdout_capture.getvalue()

# --- Scenario: Responds to messages

@given('my text includes {keyword}')
def step(context, keyword):
    context.keyword = keyword
    context.history = []


@when('I speak with Marvin')
def step(context):
    handle_response(context.history, f'stuff {context.keyword} and things')


@then('I expect response to be non-blank')
def step(context):
    assert context.stdout_capture.getvalue() != ''


# --- Scenario: Scenario Outline: Keywords

#    Given my text includes <keyword>
#    When I speak with Marvin
#    Then I expect response to include <response_keyword>
#    Then something something
#    And mumble mumble


@then('I expect response to include {response_keyword}')
def step(context, response_keyword):
    assert response_keyword in context.stdout_capture.getvalue()


@then('something something')
def step(context):
    pass


@then('mumble mumble')
def step(context):
    pass
