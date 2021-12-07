Feature: spellcastmanager-context

  Scenario: request ruletext with existing spell
    Given an english speaking user
    When the user says "Give me the ruletext for the spell fireball"
    Then mycroft should send the message "{complete_intent_failure}"

  Scenario: Start Spellcastmanager
    Given an english speaking user
    When the user says "Open the spellcast manager"
    Then "spellcastmanager-skill" should reply with dialog from "spellcastmanager.started.dialog"

  Scenario: request ruletext with existing spell
    Given an english speaking user
    When the user says "Give me the ruletext for the spell fireball"
    Then "spellcastmanager-skill" should reply with dialog from "long.ruletext.dialog"

  Scenario: Fixture Stop Spellcastmanager
    Given an english speaking user
    When the user says "Close the spellcast manager"
    Then "spellcastmanager-skill" should reply with dialog from "spellcastmanager.stopped.dialog"

  Scenario: request ruletext with existing spell
    Given an english speaking user
    When the user says "Give me the ruletext for the spell fireball"
    Then mycroft should send the message "{complete_intent_failure}"