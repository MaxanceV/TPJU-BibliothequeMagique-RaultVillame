Feature: Gestion des quetes

  Scenario: Ajouter XP a une quete
    Given une quete "Sauver le village"
    When j ajoute 10 points XP
    Then le XP de la quete est 10

  Scenario: Calcul du XP total avec bonus
    Given une quete "Sauver le village" avec une recompense de 20 XP
    When j ajoute 10 points XP
    Then le XP total avec bonus est 30

  Scenario: Valeurs XP invalides ignorees
    Given une quete "Sauver le village"
    When j ajoute -5 points XP
    And j ajoute 0 points XP
    Then le XP de la quete est 0

  Scenario: Une recompense ne peut appartenir qu a une seule quete
    Given deux quetes "Q1" et "Q2"
    And une recompense "Couronne" avec 50 XP
    When j assigne la recompense a la quete "Q1"
    And j assigne la recompense a la quete "Q2"
    Then la quete "Q1" n a pas de recompense
    And la recompense appartient a la quete "Q2"