[Français](README.md) | **English**

# SOMIG — Solar Maintenance and Intervention Guide

Conversational diagnosis and intervention guide for off-grid solar systems.

The technician describes the observed problem. SOMIG asks the diagnostic questions in a useful order, identifies the probable cause and proposes the intervention procedure.

> Status: in development — MVP in progress.

## Why

In the field, most faults come from a small number of known causes. An experienced technician identifies them in minutes; a junior technician may spend a day on it or replace healthy equipment. SOMIG makes this experience available to everyone, on a channel they already use: WhatsApp.

## How it works

1. The technician sends a message describing the symptom (text, photo of a display, a measurement).
2. SOMIG matches the symptom against the knowledge base.
3. It guides the diagnosis through successive questions (measurements to take, points to check).
4. It proposes the probable cause, the intervention procedure and safety precautions.

## MVP scope

- Channel: WhatsApp Business.
- Knowledge base: the 20 most frequent faults on off-grid solar systems (solar home kits, charge controllers, inverters, lead-acid and LiFePO4 batteries).
- Format: one JSON file per fault, readable and editable by a technician.

## Access

| User | Access | Cost |
|---|---|---|
| Technician | Guided diagnosis, full knowledge base | Free |
| Installation company | Intervention tracking per technician, reports | Subscription |
| Manufacturer, distributor | Anonymized fault statistics by equipment | Subscription or one-off report |

## Repository structure

```
somig/
├── knowledge-base/      # Fault cases in JSON
│   └── schema.json      # Validation schema for a case
├── engine/              # Diagnostic logic
├── channels/whatsapp/   # WhatsApp Business connector
├── docs/
├── README.md
├── README.en.md
├── LICENSE
└── CONTRIBUTING.md
```

## Contributing

Contributions from technicians come first: new fault cases, procedure corrections, field feedback.

Each contributor signs a Contributor License Agreement (CLA) before their first merge. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Safety

SOMIG is a diagnostic aid. It does not replace training or electrical safety rules. Every intervention remains the technician's responsibility.

## License

Code licensed under [AGPL-3.0](LICENSE). Any use of this code in a network-accessible service requires publishing modifications under the same license.

A commercial license is available for uses incompatible with the AGPL. Contact: weareoshu.project@gmail.com.

## Project

Part of [OSHU — Open Solar Hub](https://github.com/oshu-africa).

---

© 2026 ON-Tech. Copyright holder of the code.
