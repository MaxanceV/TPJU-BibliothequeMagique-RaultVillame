Feature: Mission - Quête et puissance du Magicien
  En tant que Magicien
  Je veux terminer une mission liée à une quête
  Afin d'ajouter l'xp de la quête à ma puissance

  Scenario Outline: Terminer une mission ajoute l'xp total (avec bonus) à la puissance
    Given un magicien nommé <nom>
    And sa puissance de base est <puissance_base>
    And une quête "<titre_quete>" avec <xp> xp
    And une récompense "<nom_recompense>" donnant <bonus> xp
    When le magicien termine la mission
    Then la puissance du magicien doit être de <puissance_attendue>

    Examples:
      | nom   | puissance_base | titre_quete           | xp  | nom_recompense | bonus | puissance_attendue |
      | Harry | 10             | Sauver le village     | 20  | Medaille       | 5     | 35                |
      | Ron   | 10             | Explorer la grotte    | 0   | Badge          | 10    | 20                |
      | Rogue | 50             | Vaincre le dragon     | 100 | Couronne       | 0     | 150               |

  Scenario: Terminer une mission sans récompense ajoute seulement l'xp de base
    Given un magicien nommé Harry
    And sa puissance de base est 10
    And une quête "Apprendre un sort" avec 15 xp
    When le magicien termine la mission
    Then la puissance du magicien doit être de 25
