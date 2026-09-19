# Validation Summary

| Candidate | Predictions | Accuracy |
|---|---:|---:|
| Confidence ≥70, HOME/AWAY, gap ≥10 | 4,100 | 55.6% |
| Confidence ≥70, HOME/AWAY, gap ≥20 | 2,344 | ~61% |
| Confidence ≥70, HOME/AWAY, gap ≥30 | 1,011 | ~64% |

The ≥20 breakpoint produced a substantial reliability improvement over ≥10 while retaining much more coverage than ≥30.

The frozen v1 layer is intended to improve **ranking**, especially among stronger predictions. It does not claim that the adjusted score is a calibrated probability and does not replace the base prediction engine.
