-- Portfolio-safe example. No production credentials or endpoints included.
SELECT
    fixture_date, country, league_name, predicted_result, result,
    result_correct, result_confidence_score, strength_difference,
    prediction_model_version
FROM fact_model_reliability
WHERE settlement_status = 'SETTLED'
  AND result_correct IS NOT NULL
ORDER BY fixture_date, fixture_id;
