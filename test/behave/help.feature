Feature: spellcastmanager-context

  Scenario: request help and selecting option one
    Given an english speaking user
    When the user says "what does spellcastmanager do "
    Then "spellcastmanager-skill" should reply with dialog from "help.get.dialog"

  Scenario: selecting option one
    Given a 25 second timeout
    Given an english speaking user
    When the user says "Option One"
    Then "spellcastmanager-skill" should reply with dialog from "help.option.all"

  # - different help utterances
  Scenario Outline: request help
    Given an english speaking user
    When the user says "<help>"
    Then "spellcastmanager-skill" should reply with dialog from "help.get.dialog"

    Examples: help
      | help                                  |
      | what does spellcastmanager do         |
      | what does the spellcast manager do    |
      | what does spellcastmanager            |
      | what can i do with spellcastmanager   |
      | i need help with spellcastmanager     |
      | i need help with the spellcastmanager |
      | how do i use the spellcastmanager     |
      | spellcastmanager help                 |
      | spellcatmanager help please           |
