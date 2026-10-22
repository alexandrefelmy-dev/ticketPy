---
name: lint
description: Valide le code Python avec pylint et les fichiers Markdown avec pymarkdown. À utiliser quand l'utilisateur tape /lint, demande de « linter », « valider le code », « vérifier la qualité du code » ou « vérifier le README », ou après une modification de fichiers .py ou .md pour proposer une validation avant commit.
---

# Validation du code avec pylint et pymarkdown

Objectif : analyser les fichiers Python avec pylint et les fichiers Markdown avec pymarkdown, présenter les problèmes trouvés, puis **demander à l'utilisateur** ce qu'il veut corriger. Ne jamais modifier les fichiers sans son accord.

## Étapes

1. **Vérifier que les linters sont installés**
   - Lancer `python -m pylint --version` et `python -m pymarkdown version`.
   - Pour chaque outil absent, demander à l'utilisateur (avec AskUserQuestion) s'il veut l'installer : `python -m pip install pylint` ou `python -m pip install pymarkdownlnt`. S'il refuse, ignorer ce type de fichier et continuer avec l'autre.

2. **Choisir les fichiers à analyser**
   - Si l'utilisateur a passé des arguments (`$ARGUMENTS`), analyser ces fichiers.
   - Sinon, analyser les fichiers `.py` et `.md` modifiés (`git status --porcelain`) ; s'il n'y en a aucun, analyser tous les fichiers `.py` et `.md` suivis par git (`git ls-files "*.py" "*.md"`).
   - Ne pas analyser les fichiers de `.claude/`.

3. **Lancer l'analyse**
   - Python : `python -m pylint <fichiers .py> --output-format=text --score=y`
   - Markdown : `python -m pymarkdown scan <fichiers .md>`
   - Si un fichier de configuration existe (`.pylintrc`, `.pymarkdown.json`, ou une section `[tool.pylint]` / `[tool.pymarkdown]` dans `pyproject.toml`), les outils l'utilisent automatiquement : ne pas passer d'autres options.

4. **Présenter le résultat** (en français)
   - Python : la note globale (ex. `7.85/10`), puis un tableau des problèmes regroupés par catégorie : Erreurs (E), Avertissements (W), Refactoring (R), Convention (C), avec le lien `fichier:ligne`, le code (ex. `C0116`) et une explication courte. Signaler en premier les erreurs (E) et avertissements (W), qui peuvent cacher de vrais bugs.
   - Markdown : le nombre de problèmes, puis un tableau avec le lien `fichier:ligne`, la règle (ex. `MD022`) et une explication courte.

5. **Demander la validation à l'utilisateur**
   Utiliser AskUserQuestion pour proposer :
   - Corriger tous les problèmes
   - Corriger seulement les erreurs et avertissements Python (E/W)
   - Choisir les problèmes à corriger un par un
   - Ne rien corriger (le code est validé tel quel)

6. **Appliquer les corrections choisies**, puis relancer les linters et comparer avec le résultat précédent (note pylint, nombre de problèmes Markdown).
   - Ne pas désactiver une règle (`# pylint: disable=...`, configuration pymarkdown) sans le proposer explicitement à l'utilisateur.
   - Pour le Markdown, ne changer que la mise en forme, jamais le contenu du texte.
   - Ne pas faire de commit : laisser l'utilisateur décider.
