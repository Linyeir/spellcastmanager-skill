Feature: spellcast manager read single detail

    Scenario: request information with existing spell
        Given an english speaking user
         When the user says "I want some information about the spell fireball"
         Then "spellcastmanager-skill" should reply with dialog from "get.single.detail.request.detail.dialog"

    Scenario: name detail
        Given an english speaking user
         Given a 20 second timeout
         When the user says "range"
         Then "spellcastmanager-skill" should reply with dialog from "get.single.detail.range.dialog"
    
    