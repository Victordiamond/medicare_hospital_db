Measured PostgreSQL 18 plan outputs are saved in `plan-before-index.csv`, `plan-after-index.csv`, and `completed-payment-plan.csv`. The completed-payment aggregation used a sequential scan of the one matching payment row, followed by a hash aggregate. Execution time was 0.091 ms. The partial covering index exists, but this tiny table gives the planner no reason to use it. This is verified evidence, not a performance improvement claim.

Screenshots are still pending. The sample is too small for a meaningful benchmark.
