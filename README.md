# PMP Prep

Hard-level PMP exam preparation built around a single case project, Lodestar (an AI chief-of-staff product, originally called Keel).

- `question-bank/` holds the questions as JSON batches (`bank1.json`, `bank2.json`, ...) with a README describing the format. Target: 1000 questions.
- `simulator/index.html` is the exam simulator: full and half timed sittings in the July 2026 format (180 questions, 240 minutes, two breaks), adaptive practice, and a study plan that ranks weak topics and replays missed questions. It loads the `bank*.json` files next to it.

The real PMP exam is not adaptive. The adaptive mode here is a practice aid only.

Related documents: the Lodestar PRD case study and the Case Drill are published as claude.ai artifacts in the owner's account.

## How the bank is built (same pattern as Keel)

- **Task queue:** `question-bank/COVERAGE.md` lists every outline task with its target and gap. The biggest gaps are the next batch's tasks. Regenerate with `tools/coverage.py`.
- **Bounded workers:** each batch is a separate `bankN.json` written by one worker, so a failed batch never damages another.
- **Independent reviewer:** a second agent answers every question without seeing the marked answer, recomputes the math, and flags disagreements before a batch ships.
- **Corrections log:** every mistake caught is recorded in `question-bank/corrections.jsonl` and distilled into `question-bank/CONVENTIONS.md`, which all writers and the reviewer follow.
- **Learning from you:** the simulator keeps the questions you miss and ranks your weak topics into a study plan.
