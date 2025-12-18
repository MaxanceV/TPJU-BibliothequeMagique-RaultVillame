Feature: Factory Method - Invocation de livres
  En tant que Magicien
  Je veux invoquer un livre magique
  Afin de l'obtenir automatiquement dans mon inventaire

  Scenario: Un magicien invoque un livre classique
    Given un magicien nommé Gandalf
    When il invoque un livre "Grimoire Classique"
    Then le magicien possède le livre "Grimoire Classique"

  Scenario: Un magicien de feu invoque un livre de feu
    Given un magicien de feu nommé Azar
    When il invoque un livre "Grimoire Incandescent"
    Then le magicien possède un livre de feu "Grimoire Incandescent"
