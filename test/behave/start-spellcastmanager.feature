Feature: start-spellcastmanager

  Scenario: English Start Spellcastmanager
    Given an english speaking user
     When the user says "Start spellcast manager."
     Then "start-spellcastmanager" should reply with "spellcastmanager.dialog"

  Scenario: German Start Spellcastmanager
    Given an german speaking user
     When the user says "Starte den Spellcast Manager."
     Then "start-spellcastmanager" should reply with dialog from "spellcastmanager.dialog"