**Français** | [English](README.en.md)

# SOMIG — Solar Maintenance and Intervention Guide

Guide de diagnostic et d'intervention pour les systèmes solaires hors réseau, par assistant conversationnel.

Le technicien décrit le problème observé. SOMIG pose les questions de diagnostic dans l'ordre utile, identifie la cause probable et propose la procédure d'intervention.

> Statut : en développement — MVP en cours.

## Pourquoi

Sur le terrain, la majorité des pannes relèvent d'un petit nombre de causes connues. Un technicien expérimenté les identifie en quelques minutes ; un technicien junior peut y passer une journée ou remplacer un équipement sain. SOMIG met cette expérience à disposition de tous, sur un canal déjà utilisé : WhatsApp.

## Fonctionnement

1. Le technicien envoie un message décrivant le symptôme (texte, photo de l'afficheur, mesure).
2. SOMIG rapproche le symptôme des cas de la base de connaissances.
3. Il guide le diagnostic par questions successives (mesures à prendre, points à vérifier).
4. Il propose la cause probable, la procédure d'intervention et les précautions de sécurité.

## Périmètre du MVP

- Canal : WhatsApp Business.
- Base de connaissances : les 20 pannes les plus fréquentes sur les systèmes solaires hors réseau (kits domestiques, régulateurs, onduleurs, batteries plomb et LiFePO4).
- Format : un fichier JSON par panne, lisible et modifiable par un technicien.

## Accès

| Utilisateur | Accès | Coût |
|---|---|---|
| Technicien | Diagnostic guidé, base de connaissances complète | Gratuit |
| Entreprise d'installation | Suivi des interventions par technicien, rapports | Abonnement |
| Fabricant, distributeur | Statistiques de pannes anonymisées par équipement | Abonnement ou rapport ponctuel |

## Structure du dépôt

```
somig/
├── knowledge-base/      # Cas de pannes au format JSON
│   └── schema.json      # Schéma de validation d'un cas
├── engine/              # Logique de diagnostic
├── channels/whatsapp/   # Connecteur WhatsApp Business
├── docs/
├── README.md
├── README.en.md
├── LICENSE
└── CONTRIBUTING.md
```

## Contribuer

Les contributions de techniciens sont prioritaires : nouveaux cas de pannes, corrections de procédures, retours de terrain.

Chaque contributeur signe un accord de contribution (CLA) avant la première fusion. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Sécurité

SOMIG est une aide au diagnostic. Il ne remplace ni la formation ni les règles de sécurité électrique. Toute intervention reste sous la responsabilité du technicien.

## Licence

Code sous licence [AGPL-3.0](LICENSE). Toute exploitation de ce code dans un service accessible en ligne impose la publication des modifications sous la même licence.

Une licence commerciale est disponible pour les usages incompatibles avec l'AGPL. Contact : weareoshu.project@gmail.com.

## Projet

Fait partie de [OSHU — Open Solar Hub](https://github.com/oshu-africa).

---

© 2026 ON-Tech. Titulaire des droits sur le code.
