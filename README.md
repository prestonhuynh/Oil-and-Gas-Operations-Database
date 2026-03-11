# **Oil and Gas Operations Database**
A relational SQL project analyzing capital project operations for a fictional Oil & Gas operator, Meridian Energy Group. Built to answer real business questions an operations director would act on.

## Tools
 • Python (data generation: pandas, numpy, faker)\
 • SQLite\
 • DBeaver

## Database Structure
projects — Core project registry. One row per project.\
 • project_id, project_type, region, manager, budget, status

labor — Labor entries logged against projects.\
 • labor_id, project_id, trade, hours, rate, date

materials — Material purchases logged against projects.\
 • material_id, project_id, material_type, quantity, unit_cost, date

milestones — Milestone tracking with planned vs actual dates.\
 • milestone_id, project_id, milestone, planned_date, actual_date, slippage_days

## Business Questions & Insights
### Which manager has the best on-time rate?
Jamie Sullivan, OE leads all managers with a 42.9% on-time rate across 7 projects with 3 completed. Adrian Cardenas, PE sits at the bottom with 0 completed projects across 7 assigned — every project is either active, delayed, or over budget. The gap between top and bottom performers suggests significant variance in project execution quality across the management team.

### Which trade consumes the most labor cost?
Drilling Engineers carry the highest total cost driven by volume of hours. Notably, Heavy Equipment Operators command the highest average rate at $102.29/hr despite ranking third in total cost — indicating fewer but more expensive engagements.

### Which projects have milestone slippage over 2 weeks?
40 milestone entries exceeded 14 days of slippage. The worst offender was OG-1038, a Well Drilling project in Eagle Ford managed by Yesenia Evans, OE, with 58 days of slippage on Project Closeout. Project Closeout and Quality Inspection milestones appeared most frequently in the slippage list, suggesting late-stage execution is the most common breakdown point across the portfolio. Alec Ramirez, OE appeared most frequently across slipped milestones.

### Which region runs most over budget?
Permian Basin showed the highest budget variance at 86.3% over budget with an average budget of $8,754,773.50 against average labor and material costs of $12,329.32. Eagle Ford had the lowest variance at 74.5% — still significantly over budget, indicating a portfolio-wide cost control issue rather than a region-specific one.

## Files
 • generate_data.py — Synthetic data generator\
 • queries.sql — All business queries with comments\
 • data/ — Generated CSVs for all four tables\
 • oil_gas_operations.db — SQLite database file
