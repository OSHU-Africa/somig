# Base de connaissances SOMIG

Un fichier JSON par cas de panne, dans le dossier `cases/`, nommé `SOMIG-XXX-titre-court.json`.

## Structure d'un cas

| Champ | Contenu |
|---|---|
| `id`, `version` | Identifiant `SOMIG-001` et numéro de version |
| `titre` | Titre en français (obligatoire) et en anglais (facultatif) |
| `categorie` | batterie, regulateur, onduleur, panneau, cablage_protection, charge, paygo, autre |
| `systemes` | kit_domestique, usage_productif, pompage, institutionnel |
| `frequence`, `gravite` | Fréquence terrain et gravité |
| `symptomes` | Ce qu'on observe + mots-clés tels qu'un technicien les écrirait sur WhatsApp |
| `outils`, `securite` | Matériel requis et précautions |
| `diagnostic` | Arbre de questions : chaque réponse mène à une étape (`E2`) ou à une cause (`C1`) |
| `causes` | Cause identifiée, procédure d'intervention, pièces, durée, escalade éventuelle |
| `notes_terrain` | Retour d'expérience libre |

Le fichier `cases/SOMIG-000-exemple.json` montre un cas complet. Il est fictif et sert de modèle.

## Règles

- Le diagnostic commence toujours par l'étape `E1`.
- Une mesure précise toujours son unité (`V`, `A`, `W`…).
- Les mots-clés reprennent le langage réel du terrain, fautes et expressions locales comprises.
- Tout cas doit être valide selon `schema.json` avant fusion.
