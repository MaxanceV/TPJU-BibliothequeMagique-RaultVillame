Feature: Collaboration entre le Magicien et son Livre
En tant que Magicien 
Je veux acquérir un livre magique
Afin d'augmenter la puissance totale de mes sorts

Scenario Outline: Calcul de la puissance d'attaque avec un livre équipé
Given un magicien nommé <nom>
And un livre nommé <titre> avec <points_livre> points de magie
When <nom> prend le livre
Then sa puissance de sort doit être de <total_attendu>

Examples:
| nom   | titre                | points_livre | total_attendu |
| Harry | Grimoire de Poudlard | 50           | 60            |
| Ron   | Petit Grimoire       | 20           | 30            |
| Rogue | Super Grimoire       | 100          | 110           |