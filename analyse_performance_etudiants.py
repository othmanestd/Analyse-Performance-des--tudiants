# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Génération des données synthétiques
np.random.seed(42)
nombre_etudiants = 100

heures_etude = np.random.randint(0, 21, nombre_etudiants)
taux_presence = np.random.randint(60, 101, nombre_etudiants)
exercices_completes = np.random.randint(0, 21, nombre_etudiants)
heures_sommeil = np.random.uniform(4, 10, nombre_etudiants).round(1)
note_finale = (
    0.3 * heures_etude +
    0.2 * (taux_presence / 10) +
    0.3 * exercices_completes +
    0.2 * heures_sommeil +
    np.random.normal(0, 2, nombre_etudiants)
).round(1)

data = pd.DataFrame({
    'heures_etude': heures_etude,
    'aux_presence': taux_presence,
    'exercices_completes': exercices_completes,
    'heures_sommeil': heures_sommeil,
    'note_finale': note_finale
})

# Sauvegarde du jeu de données
data.to_csv("performances_etudiants.csv", index=False)
print("Le jeu de données a été généré et sauvegardé sous le nom 'performances_etudiants.csv'.")

# Partie 1 : Exploration et analyse des données
print("\n--- Exploration et Analyse des Données ---")
print("Les 5 premières lignes du dataset :")
print(data.head())

moyenne_notes_finales = data['note_finale'].mean()
print(f"Moyenne des notes finales : {moyenne_notes_finales:.2f}")

moyenne_heures_etude = data['heures_etude'].mean()
print(f"Moyenne des heures d'étude : {moyenne_heures_etude:.2f}")

# Partie 2 : Visualisation des données
print("\n--- Visualisation des Données ---")

# Graphique : relation entre heures d'étude et notes finales
plt.figure(figsize=(8, 6))
sns.scatterplot(x='heures_etude', y='note_finale', data=data, color='blue')
plt.title("Relation entre heures d'étude et notes finales")
plt.xlabel("Heures d'étude (par semaine)")
plt.ylabel("Note finale")
plt.grid(True)
plt.show()

# Graphique : notes finales selon le taux de présence
plt.figure(figsize=(8, 6))
sns.boxplot(x=pd.cut(data['aux_presence'], bins=4), y='note_finale', data=data)
plt.title("Notes finales selon le taux de présence")
plt.xlabel("Catégorie de taux de présence")
plt.ylabel("Note finale")
plt.grid(True)
plt.show()

# Partie 3 : Modélisation prédictive
print("\n--- Modélisation Prédictive ---")

X = data[['heures_etude']]
y = data['note_finale']

# Séparation des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Prédiction pour un étudiant étudiant 10 heures par semaine
prediction = model.predict([[10]])
print(f"Prédiction pour un étudiant étudiant 10 heures par semaine : {prediction[0]:.2f}")

# Évaluation du modèle
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Erreur quadratique moyenne (RMSE) : {rmse:.2f}")
