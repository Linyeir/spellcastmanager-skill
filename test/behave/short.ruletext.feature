Feature: spellcast manager read short ruletext

    Scenario Outline: request short ruletext with existing spell
        Given an english speaking user
         When the user says "<request_short_ruletext_with_existing_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "short.ruletext.dialog"

    Examples: request short ruletext with existing spell            
        | request_short_ruletext_with_existing_spell                        |
        | Give me the details to the spell fireball                         |
        | Tell me the details to the spell bless                            |
        | Read me the details to the spell burning hands                    |
        | Give me a short version of the spell confusion                    |
        | Tell me the compact version of the spell create or destroy water  |
        | Read me the compact descripton of the spell darkness              |
        | Give me a short explanation of the spell detect evil and good     |
        | Give me the summary of the spell divine favor                     |
        | What does the spell eldritch blast do in short                    |
        | Explain the spell gate in short                                   |
        | details for the spell gentle repose                               |
        | short ruletext for the spell guardian of faith                    |
        | short version of the spell gust of wind                           |
        | short description of the spell heal                               |



    Scenario Outline: request short ruletext with invalid spell
        Given an english speaking user
         When the user says "<request_short_ruletext_with_invalid_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "ruletext.invalid.spell.dialog"

    Examples: request short ruletext with invalid spell            
        | request_short_ruletext_with_invalid_spell                         |
        | Give me the details to the spell acid cloud                       |
        | Tell me the details to the spell arcane                           |
        | Read me the details to the spell banish                           |
        | Give me a short version of the spell fire                         |
        | Tell me the compact version of the spell kill                     |
        | Read me the compact descripton of the spell hall                  |
        | Give me a short explanation of the spell help                     |
        | Give me the summary of the spell climate change                   |
        | What does the spell heroin do in short                            |
        | Explain the spell ice in short                                    |
        | details for the spell protection                                  |
        | short ruletext for the spell kill                                 |
        | short version of the spell vaccination                            |
        | short description of the spell arcane                             |

    

    Scenario Outline: request short ruletext without stating spell
        Given an english speaking user
         When the user says "<request_short_ruletext_without_stating_spell>"
         Then "spellcastmanager-skill" should reply with dialog from "ruletext.fallback.dialog"
    
    Examples: request short ruletext without stating spell
        | request_short_ruletext_without_stating_spell                      |
        | Give me the details to the spell                                  |
        | Tell me the details to the spell                                  |
        | Read me the details to the spell                                  |
        | Give me a short version of the spell                              |
        | Tell me the compact version of the spell                          |
        | Read me the compact descripton of the spell                       |
        | Give me a short explanation of the spell                          |
        | Give me the summary of the spell                                  |
        | What does the spell do in short                                   |
        | Explain the spell in short                                        |
        | details for the spell                                             |
        | short ruletext for the spell                                      |
        | short version of the spell                                        |
        | short description of the spell                                    |

        # unterscheidung zu detailfragen mit kontext?!?!