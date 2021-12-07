Feature: spellcast manager read short ruletext

  Scenario: Start Spellcastmanager
    Given an english speaking user
    When the user says "Open the spellcast manager"
    Then "spellcastmanager-skill" should reply with dialog from "spellcastmanager.started.dialog"

  Scenario: short description of spell
    Given an English speaking user
    When the user says "ruletext for fireball"
    Then "spellcastmanager-skill" should reply with "i will tell you about {spell}"

  Scenario: Stop Spellcastmanager
    Given an english speaking user
    When the user says "Close the spellcast manager"
    Then "spellcastmanager-skill" should reply with dialog from "spellcastmanager.stopped.dialog"

