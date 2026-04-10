# BENCHMARK - Comparaison des performances Bruteforce vs Optimized
#
# IMPORTS
#   - csv, time, matplotlib
#   - bruteforce_algo depuis bruteforce.py
#   - optimized_algo depuis optimized.py
#
# CONSTANTE
#   - BUDGET = 500.0
#
# FONCTION parse_csv(filepath)
#   - Ouvrir le fichier CSV
#   - Pour chaque ligne : parser nom, prix, profit
#   - Ignorer les lignes invalides (ValueError)
#   - Ignorer les prix <= 0 et profits <= 0
#   - Retourner la liste des actions nettoyées
#
# FONCTION main()
#   - Charger toutes les actions depuis data/dataset-short.csv via parse_csv
#   - Initialiser deux listes vides : times_bf, times_opt
#   - Initialiser sizes = [1, 2, ..., 20]
#
#   - POUR n allant de 1 à 20 :
#       - subset = les n premières actions
#
#       - Démarrer chronomètre
#       - Exécuter bruteforce_algo(subset, BUDGET)
#       - Stopper chronomètre → ajouter durée à times_bf
#
#       - Démarrer chronomètre
#       - Exécuter optimized_algo(subset, BUDGET)
#       - Stopper chronomètre → ajouter durée à times_opt
#
#       - Afficher : n, temps bruteforce, temps optimized
#
#   - Créer le graphique matplotlib :
#       - Axe X : temps d'exécution (secondes) — échelle logarithmique
#       - Axe Y : nombre d'actions
#       - Courbe rouge  : bruteforce  O(2^n)
#       - Courbe verte  : optimized   O(n log n)
#       - Titre, légende, grille
#       - Sauvegarder en benchmark.png
#
# POINT D'ENTRÉE
#   - Si __name__ == "__main__" : appeler main()
