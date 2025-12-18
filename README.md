# 📚 Bibliothèque Magique - Projet Agilité

Ce dépôt retrace l'évolution d'un système de gestion de grimoires magiques, passant d'une initiation sous **Java/BlueJ** à un environnement professionnel en **Python**.

## 📂 Structure du Projet

Le dépôt est organisé pour refléter la transition entre les deux semestres d'apprentissage :

* **`java/`** : Contient les sources (`.java`) et les fichiers de configuration BlueJ du premier semestre.
* **`python/`** : Dossier principal du second semestre incluant le code métier et les tests.
    * `magicien.py` & `livre_magique.py` : Classes principales.
    * `features/` : Tests d'acceptation (User Stories) écrits en Gherkin/Behave.
    * `tests/` : Tests unitaires robustes utilisant le framework `unittest`.
* **Racine** : Contient le tutoriel de référence au format PDF.

## 📖 Tutoriel de Référence
Pour comprendre la progression du projet, veuillez consulter la dernière version du document située à la racine : 
👉 **`Tutoriel Agilité 1 V3.0.pdf`**

### Sommaire des points abordés :
1.  **Fondamentaux POO** : Création de classes et méthodes sous BlueJ.
2.  **Tests Automatisés** : Introduction à la "Barre Verte" et aux Fixtures.
3.  **Migration Python** : Retranscription du code et usage de VS Code.
4.  **Agilité & BDD** : Rédaction de User Stories avec Behave (Given/When/Then).
5.  **Associations Complexes** : Implémentation d'une relation bidirectionnelle "0..1 à *" (un magicien peut posséder plusieurs livres).
6.  **Qualité Logicielle** : Refactoring (Rename, Extract Method) et exécution des tests en ligne de commande.



## 🚀 Exécution des Tests (Ligne de commande)
Depuis le dossier `python/` :
* **Tests Unitaires** : `python -m unittest tests.test_magicien`
* **Tests Fonctionnels** : `python -m behave`

---

### 🤖 Note sur l'IA
Ce projet a bénéficié de la collaboration de **Gemini**, agissant en tant que partenaire de réflexion et assistant au développement (Pair Programming) pour l'aide à la retranscription en Python, et la rédaction de la documentation.

---
**Auteurs :** Maxance Villame & Justine Rault 
**Université Paris Dauphine | PSL**
**Date :** 18/12/2025