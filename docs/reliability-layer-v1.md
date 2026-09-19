# ScoreSync Reliability Layer v1

| Predicted result | Absolute strength gap | Adjustment |
|---|---:|---:|
| HOME / AWAY | 0–19 | 0 |
| HOME / AWAY | 20–29 | +6 ranking points |
| HOME / AWAY | 30+ | +10 ranking points |
| DRAW | any | 0 |

## Guardrails
- Preserve raw confidence and raw 1X2 probabilities.
- Calculate reliability score separately.
- Do not feed the adjusted score back into Dixon-Coles probability normalisation.
- Do not describe the adjusted score as a probability.
- Null strength means no strength adjustment.
- Version the layer for later comparison.

## Deferred from v1
League reliability, DRAW-specific penalties, small-gap penalties, probability calibration and model-version interactions require more evidence.
