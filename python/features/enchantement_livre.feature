#Author : Justine Rault & Maxance Villame

@tag
Feature: Enchantement du Grimoire
En tant que Magicien débutant
Je veux pouvoir enchanter mon livre de magie
Afin d'augmenter mon potentiel mystique

Scenario : Augmentation des points de magie par enchantement
Given un livre nommé "Grimoire de Poudlard" avec 50 points de magie
When un magicien enchante le livre
Then le livre doit posséder 60 points de magie