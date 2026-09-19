# Methodology

## Analytical objective
Determine whether ScoreSync's existing result-confidence score could be made more useful for ranking predictions by combining it with independently derived contextual signals.

## Data validation
The private analytical export contained 16,293 fixture-level rows and 16,293 unique fixture IDs. Date coverage, duplicates and missing analytical fields were checked before rule testing.

## Discovery in Power BI
Power BI was used for baseline accuracy, confidence bands, weekly trends, outcome behaviour, strength-gap bands and league/country diagnostics. Sample-size eligibility rules reduced over-interpretation of tiny groups.

## Controlled threshold tests
Only one dimension was changed at a time. Confidence thresholds were tested while strength/outcome conditions were fixed; strength thresholds were then tested while confidence/outcome conditions were fixed.

## Chronological validation
Candidate rules were evaluated on later observations rather than relying on random train/test mixing. This better reflects the operational question: does a rule discovered from earlier fixtures continue to help on later fixtures?

## Ablation and simplification
Small-gap penalties, DRAW penalties and league modifiers were investigated. Components without sufficiently stable incremental value were excluded from v1.

## Final design principle
The existing confidence score remains the base. Strength separation is used only as a conservative ranking reinforcement for HOME/AWAY predictions. The resulting score is not presented as a calibrated probability.
