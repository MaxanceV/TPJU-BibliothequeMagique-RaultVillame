Feature: Gestion des récompenses

  Scenario: Création d'une récompense
    Given une récompense "Épée légendaire" avec 100 XP
    Then le nom de la récompense est "Épée légendaire"
    And le bonus XP est 100
    And la récompense n'est liée à aucune quête
