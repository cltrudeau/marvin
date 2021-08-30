@smoke @regression
Feature: Chatting with Marvin
    As a user I want to chat with Marvin in order to hear sarcastic replies

# Comment line
Scenario: Repeated text
    Given I have spoken to Marvin before
    When I repeat myself
    Then I should be told I'm repeating

#Scenario Outline: Keywords
#    Given my text includes <keyword>
#    When I speak with Marvin
#    Then I expect response to include <response_keyword>
#    Then something something
#    And mumble mumble
#
#Examples: 
#    | keyword | response_keyword |
#    | life    | life             |
#    | Life    | life             |
#    | feel    | depressed        |
#    | marvin  | level            |
#    | sad     | capacity         |
