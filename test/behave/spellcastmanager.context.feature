Feature: spellcastmanager-context

  Scenario Outline: Start Spellcastmanager
    Given an english speaking user
     When the user says "Open the spellcast manager"
     Then "spellcastmanager-skill" should reply with dialog from "spellcastmanager.started.dialog"

  Scenario Outline: Start Spellcastmanager
    Given an english speaking user
     When the user says "Close the spellcast manager"
     Then "spellcastmanager-skill" should reply with dialog from "spellcastmanager.stopped.dialog"