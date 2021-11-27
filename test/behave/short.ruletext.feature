Feature: short ruletext
    Scenario: short description of spell
        Given an English speaking user
         When the user says "ruletext for fireball"
         Then "spellcastmanager-skill" should reply with "i will tell you about {spell}"

