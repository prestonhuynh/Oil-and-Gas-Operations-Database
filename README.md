Oil and Gas Operations Database
A relational SQL project analyzing capital project operations for a fictional O&G operator, Meridian Energy Group. Built to answer real business questions an operations director would act on.
Tools

Python (data generation: pandas, numpy, faker)
SQLite
DBeaver

Database Structure
projects — Core project registry. One row per project.

project_id, project_type, region, manager, budget, status

labor — Labor entries logged against projects.

labor_id, project_id, trade, hours, rate, date

materials — Material purchases logged against projects.

material_id, project_id, material_type, quantity, unit_cost, date

milestones — Milestone tracking with planned vs actual dates.

milestone_id, project_id, milestone, planned_date, actual_date, slippage_days

Business Questions & Insights
Which manager has the best on-time rate?
Queried completion rate per manager across all assigned projects. Results ranked by on-time percentage to identify highest and lowest performers.
Which trade consumes the most labor cost?
Drilling Engineers recorded the highest total labor cost at $802,369.90 — driven by both high hourly rates and total hours logged across projects.
Which projects have milestone slippage over 2 weeks?
Over 40 milestone entries exceeded 14 days of slippage. High slippage volume suggests scheduling assumptions are systematically underestimated across the portfolio.
Which region runs most over budget?
Permian Basin showed the highest budget variance at 86.3%, making it the highest-risk region for cost overruns in the portfolio.
Files

generate_data.py — Synthetic data generator
queries.sql — All business queries with comments
data/ — Generated CSVs for all four tables
oil_gas_operations.db — SQLite database file
