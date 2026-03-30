-- Query 1: Manger on-time rate
SELECT p.manager,
       COUNT(*) AS total_projects,
       SUM(CASE WHEN p.status = 'Completed' THEN 1 ELSE 0 END) AS completed,
       ROUND(SUM(CASE WHEN p.status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS on_time_rate_pct
FROM projects p
GROUP BY p.manager
ORDER BY on_time_rate_pct DESC;

-- Query 2: Trade labor cost
SELECT trade,
       ROUND(SUM(hours * rate), 2) AS total_labor_cost,
       SUM(hours) AS total_hours,
       ROUND(AVG(rate), 2) AS avg_rate
FROM labor
GROUP BY trade 
ORDER BY total_labor_cost DESC;

-- Query 3: Projects with milestone slippage over 2 weeks
SELECT p.project_id,
       p.project_type,
       p.region,
       p.manager,
       m.milestone,
       m.slippage_days
FROM projects p
JOIN milestones m ON p.project_id = m.project_id 
WHERE m.slippage_days > 14
ORDER BY m.slippage_days DESC;

-- Query 4: Region budget performance
SELECT
    p.region,
    COUNT(*) AS total_projects,
    ROUND(AVG(l.hours * l.rate), 2) AS avg_labor_cost,
    ROUND(AVG(m2.quantity * m2.unit_cost), 2) AS avg_material_cost,
    ROUND(AVG(p.budget), 2) AS avg_budget,
    ROUND((AVG(l.hours * l.rate) + AVG(m2.quantity * m2.unit_cost) - AVG(p.budget)) / AVG(p.budget) * 100.0, 1) AS budget_variance_pct
FROM projects p
LEFT JOIN labor l ON p.project_id = l.project_id
LEFT JOIN materials m2 ON p.project_id = m2.project_id
GROUP BY p.region
ORDER BY budget_variance_pct DESC;
