# PMP Prep

Hard-level PMP exam preparation built around a single case project, Lodestar (an AI chief-of-staff product, originally called Keel).

- `question-bank/` holds the questions as JSON batches (`bank1.json`, `bank2.json`, ...) with a README describing the format. Target: 360 questions so two full 180-question sittings overlap little.
- `simulator/index.html` is the exam simulator: full and half timed sittings in the real format (180 questions, 230 minutes, two breaks), adaptive practice, and a study plan that ranks weak topics and replays missed questions. It loads the `bank*.json` files next to it.

The real PMP exam is not adaptive. The adaptive mode here is a practice aid only.

Related documents: the Lodestar PRD case study and the Case Drill are published as claude.ai artifacts in the owner's account.
