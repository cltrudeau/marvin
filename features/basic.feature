# Basic Scenarios

@basics
Feature: Chatting with Marvin
    As a user I want to chat with Marvin in order to hear sarcastic replies

@repeat
Scenario: Repeated text
    Given I have spoken to Marvin before
    When I repeat myself
    Then I should be told I'm repeating

Scenario: Responds to messages
    Given my text includes "anything"
    When I speak with Marvin
    Then I expect response to be non-blank
