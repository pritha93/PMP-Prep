# PMP question bank

Shared question bank for the Lodestar Exam Simulator. One JSON array per batch (`bank1.json`, `bank2.json`, ...). Each question:

```json
{"d":"People|Process|Business Environment","l":1,"t":"topic tag","s":"stem","o":["A","B","C","D"],"c":1,"e":"explanation"}
```

- `d`: exam domain (target mix 42% People, 50% Process, 8% Business Environment)
- `l`: difficulty 1 to 3 (used by adaptive practice)
- `t`: topic tag (conflict, team, stakeholders, leadership, ethics, resources, agile, change, evm, schedule, risk, scope, procurement, quality, benefits, compliance, lessons)
- `c`: index of the correct option; `e`: why, including why the tempting wrong answer fails

Rules: scenario stems with one BEST answer; options of similar length; correct answer position varied (the simulator also shuffles). Target: 360 questions, so two full sittings of 180 overlap little.
Batches are published with the simulator at https://claude.ai/artifact/PvfKJTLqHc6ELwgbKhuQrG
