# Smoke test Scenarios

@smoke
Feature: Checking response keyword matching
    As a user I want Marvin to respond to certain phrases in a expected way

Scenario Outline: Keywords
    Given my text includes <keyword>
    When I speak with Marvin
    Then I expect response to include <response_keyword>
    Then something something
    And mumble mumble

Examples: 
    | keyword | response_keyword |
    | life    | life             |
    | Life    | life             |
    | feel    | depressed        |
    | marvin  | level            |
    | sad     | capacity         |
