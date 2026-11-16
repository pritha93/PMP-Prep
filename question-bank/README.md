# PMP question bank

Shared question bank for the Lodestar Exam Simulator. One JSON array per batch (`bank1.json`, `bank2.json`, ...). Each question:

```json
{"d":"People|Process|Business Environment","l":1,"t":"topic tag","s":"stem","o":["A","B","C","D"],"c":1,"e":"explanation"}
```

- `d`: exam domain (July 2026 outline: 33% People, 41% Process, 26% Business Environment)
- `l`: difficulty 1 to 3 (used by adaptive practice)
- `t`: topic tag (for example conflict, team, stakeholders, leadership, ethics, resources, agile, change, evm, schedule, risk, scope, procurement, quality, benefits, compliance, governance, issues, external, org change, improvement, knowledge, vision, expectations, communication, closure, value, finance)
- `c`: index of the correct option; `e`: why, including why the tempting wrong answer fails

Rules: scenario stems with one BEST answer; options of similar length; correct answer position varied (the simulator also shuffles). Target: 1000 questions. Real exam: 180 questions (170 scored, 10 unscored), 240 minutes, two 10-minute breaks, about 40% predictive and 60% agile/hybrid items. Source: PMI July 2026 Exam Content Outline.
Batches are published with the simulator at https://claude.ai/artifact/PvfKJTLqHc6ELwgbKhuQrG
