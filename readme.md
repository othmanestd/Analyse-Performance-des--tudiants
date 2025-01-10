# Analyse des Performances des Étudiants

Ce projet explore les performances académiques des étudiants en fonction de leurs habitudes d'étude et de leur mode de vie. Il inclut la génération de données synthétiques, leur exploration, leur visualisation, et la construction d'un modèle prédictif.

## Structure du Projet

### 1. Génération de Données Synthétiques

- **Description** : Création de données représentant les heures d'étude, le taux de présence, le nombre d'exercices complétés, les heures de sommeil, et les notes finales des étudiants.
- **Output** : Sauvegarde des données dans un fichier CSV nommé `performances_etudiants.csv`.

### 2. Exploration et Analyse des Données

- **Objectifs** :
  - Afficher les 5 premières lignes des données.
  - Calculer la moyenne des notes finales.
  - Calculer la moyenne des heures d'étude.

### 3. Visualisation des Données

- **Graphiques Générés** :
  - Relation entre les heures d'étude et les notes finales (diagramme de dispersion).
  - Comparaison des notes finales selon le taux de présence (diagramme en boîte).

### 4. Modélisation Prédictive

- **Modèle** : Régression linéaire utilisant les heures d'étude pour prédire les notes finales.
- **Prédictions** :
  - Prédiction pour un étudiant étudiant 10 heures par semaine.
  - Évaluation du modèle avec l'erreur quadratique moyenne (RMSE).

## Prérequis

Assurez-vous d'avoir les bibliothèques suivantes installées :

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Utilisation

Pour exécuter le script et générer les analyses, utilisez la commande suivante :

```bash
python analyse_performance_etudiants.py
```

## Résultats

Les résultats incluent :

- Un fichier CSV contenant les données synthétiques.
- Des graphiques illustrant les relations entre les différentes variables et les performances académiques.
- Un modèle de régression linéaire permettant de prédire les notes finales en fonction des heures d'étude.

## Auteurs

Ce projet a été réalisé par [Votre Nom].

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
