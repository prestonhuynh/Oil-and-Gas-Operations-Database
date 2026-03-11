import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random
import os

fake = Faker()
np.random.seed(42)
random.seed(42)

NUM_PROJECTS = 50
NUM_LABOR = 300
NUM_MATERIALS = 300
NUM_MILESTONES = 150

OUTPUT_DIR = 'data'
os.makedirs(OUTPUT_DIR, exist_ok=True)

PROJECT_TYPES = [
    'Well Drilling',
    'Pipeline Construction',
    'Facility Upgrade',
    'Maintenance Turnaround'
]

REGIONS = [
    'Permian Basin',
    'Eagle Ford',
    'Gulf Coast',
    'Midland'
]

STATUSES = ['Active', 'Completed', 'Delayed', 'Over Budget']

TRADES = [
    'Drilling Engineer',
    'Pipeline Welder',
    'Instrumentation Tech',
    'Heavy Equipment Operator',
    'Saftey Inspector'
]

MATERIAL_TYPES = [
    "Steel Pipe",
    "Drilling Fluid",
    "Cement",
    "Valve Assembly",
    "Safety Equipment"
]

MILESTONES = [
    "Site Preparation",
    "Equipment Mobilization",
    "Primary Operations",
    "Quality Inspection",
    "Project Closeout"
]

MANAGERS = [fake.name() + ", " + random.choice(['OE', 'PE', 'PMP'])
            for _ in range(8)]

# Generate projects table
projects = []

for i in range(NUM_PROJECTS):
    project_type = random.choice(PROJECT_TYPES)
    region = random.choice(REGIONS)
    manager =  random.choice(MANAGERS)
    budget = round(random.uniform(500_000, 15_000_000), 2)
    status = random.choice(STATUSES)

    projects.append({
        'project_id': f'OG-{1000 + i}',
        'project_type': project_type,
        'region': region,
        'manager': manager,
        'budget': budget,
        'status': status
    })

projects_df = pd.DataFrame(projects)
projects_df.to_csv(f"{OUTPUT_DIR}/projects.csv", index=False)
print(f"Projects: {len(projects_df)} rows")

# Generate labor table
labor = []

for i in range(NUM_LABOR):
    project_id = random.choice(projects_df["project_id"].tolist())
    trade = random.choice(TRADES)
    hours = round(random.uniform(8, 240), 2)
    rate = round(random.uniform(45, 150), 2)
    date = fake.date_between(start_date="-3y", end_date="today")

    labor.append({
        "labor_id": f"L-{1000 + i}",
        "project_id": project_id,
        "trade": trade,
        "hours": hours,
        "rate": rate,
        "date": date
    })

labor_df = pd.DataFrame(labor)
labor_df.to_csv(f"{OUTPUT_DIR}/labor.csv", index=False)
print(f"Labor: {len(labor_df)} rows")

# Generate materials table
materials = []

for i in range(NUM_MATERIALS):
    project_id = random.choice(projects_df["project_id"].tolist())
    material_type = random.choice(MATERIAL_TYPES)
    quantity = round(random.uniform(1, 500), 2)
    unit_cost = round(random.uniform(50, 10_000), 2)
    date = fake.date_between(start_date="-3y", end_date="today")

    materials.append({
        "material_id": f"M-{1000 + i}",
        "project_id": project_id,
        "material_type": material_type,
        "quantity": quantity,
        "unit_cost": unit_cost,
        "date": date
    })

materials_df = pd.DataFrame(materials)
materials_df.to_csv(f"{OUTPUT_DIR}/materials.csv", index=False)
print(f"Materials: {len(materials_df)} rows")

# Generate milestones table
milestones = []

for i in range(NUM_MILESTONES):
    project_id = random.choice(projects_df["project_id"].tolist())
    milestone = random.choice(MILESTONES)
    planned_date = fake.date_between(start_date="-3y", end_date="today")
    slippage_days = int(np.random.normal(7, 21))
    actual_date = planned_date + timedelta(days=slippage_days)

    milestones.append({
        "milestone_id": f"MS-{1000 + i}",
        "project_id": project_id,
        "milestone": milestone,
        "planned_date": planned_date,
        "actual_date": actual_date,
        "slippage_days": slippage_days
    })

milestones_df = pd.DataFrame(milestones)
milestones_df.to_csv(f"{OUTPUT_DIR}/milestones.csv", index=False)
print(f"Milestones: {len(milestones_df)} rows")