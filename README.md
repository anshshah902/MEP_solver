# Residential Plumbing Engine

Residential-Plumbing-Engine is a Python-based computational tool designed to automate the hydraulic design and water demand estimation for residential townships (e.g., 36-bungalow developments). By integrating National Building Code (NBC 2016) standards and Hunter’s Curve methodology, the script provides a structured workflow for sizing critical water infrastructure.
 ​🚀 Key Modules & Technical Logic
​1. Site-Wide Water Demand Analysis
​The engine calculates total site requirements by breaking down demand into Domestic (90 LPCD) and Flushing (45 LPCD) categories based on population density.
​Standard Compliance: Adheres to the Indian NBC 2016 per capita demand of 135 LPCD.
​Scalability: Handles any number of residential units and occupancy rates through dynamic user input.
​2. External Pumping & Supply Line Sizing
​Determines the theoretical diameter for supply lines by balancing pumping hours against flow velocity.
​Velocity Optimization: Designed for a standard 1.2 m/s to prevent siltation (low velocity) and water hammer (high velocity).
​Efficiency: Incorporates a 3% leakage factor to ensure infrastructure longevity.
​3. WSFU Fixture Analysis & Peak Flow
​Uses Water Supply Fixture Units (WSFU) to quantify the probability of simultaneous use across a household.
​Hunter’s Curve Implementation: Translates static fixture counts into Peak Probable Flow (L/s) using a linearized approximation of Hunter’s probability theory.
​Component Weights: Assigns weighted values to toilets (6), sinks (2), washing machines (3), and outdoor taps (3).
​4. Commercial Selection Recommendation
​The solver doesn't just provide a theoretical number; it maps calculated diameters to the nearest Standard Commercial UPVC/CPVC sizes (25mm, 32mm, 40mm, 50mm).
 ​📈 Strategic & Operational Value
​Process Efficiency: Reduces design cycle time from hours of manual tabulation to seconds of execution.
​Resource Optimization: Prevents material waste by selecting the most efficient pipe diameter, directly impacting project CAPEX.
​Data-Driven Strategy: Allows developers to simulate different occupancy scenarios and "what-if" pumping schedules before breaking ground.
