# AlgoInvest & Trade

Optimisation d'un portefeuille d'actions sous contrainte de budget (500€).
Deux approches : **bruteforce** (combinaisons exhaustives) et **optimized** (algorithme glouton).
Un benchmark compare leurs performances et génère un graphique (`benchmark.png`).

## Démarrage

```bash
pip install -r requirements.txt

python bruteforce.py data/<fichier>.csv
python optimized.py data/<fichier>.csv
python benchmark.py data/<fichier>.csv
```
