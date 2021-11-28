Feature: start-spellcastmanager

  Scenario: English Start Spellcastmanager
    Given an english speaking user
     When the user says "Start spellcast manager."
     Then "start-spellcastmanager" should reply with "spellcastmanager.dialog"