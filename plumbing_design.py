import math

def calculate_plumbing_system():
    print("--- Professional Plumbing & Pumping Design Tool ---")
    
    # --- MODULE 1: SITE-WIDE WATER DEMAND ---
    print("\n[1] Site Demand Parameters")
    num_bungalows = int(input("Enter total number of bungalows (e.g., 36): "))
    occ_per_unit = int(input("Enter occupants per bungalow (e.g., 6): "))
    lpcd = float(input("Enter Per Capita Demand (Standard 135): ")) [cite: 60, 69]
    
    total_pop = num_bungalows * occ_per_unit [cite: 69]
    daily_demand_l = total_pop * lpcd [cite: 69]
    
    # Breakdown based on NBC 2016 [cite: 70, 71, 72]
    dom_demand = total_pop * 90 
    flush_demand = total_pop * 45 
    
    print(f"Total Population: {total_pop} persons")
    print(f"Total Site Demand: {daily_demand_l:,.2f} Liters/Day")
    print(f"-> Domestic: {dom_demand:,.2f} L | Flushing: {flush_demand:,.2f} L")

    # --- MODULE 2: PUMPING & SUPPLY LINE DESIGN ---
    print("\n[2] External Pumping Design")
    pump_hours = float(input("Enter daily pumping hours (Standard 8-10): ")) [cite: 82]
    velocity_design = float(input("Enter design velocity in m/s (Standard 1.2): ")) [cite: 86]
    
    # Add 3% leakage factor [cite: 83]
    q_design_l_day = daily_demand_l * 1.03 
    flow_rate_m3s = (q_design_l_day / 1000) / (pump_hours * 3600) [cite: 84]
    
    area_req = flow_rate_m3s / velocity_design [cite: 86]
    dia_m = math.sqrt((area_req * 4) / math.pi) [cite: 86]
    dia_mm = dia_m * 1000
    
    print(f"Design Flow Rate: {flow_rate_m3s * 1000:.3f} L/s")
    print(f"Theoretical Supply Pipe Diameter: {dia_mm:.2f} mm") [cite: 86]

    # --- MODULE 3: WSFU FIXTURE COUNTER ---
    print("\n[3] Internal Fixture Unit (WSFU) Calculation")
    # Weights from your report [cite: 95]
    weights = {"bath": 6, "sink": 2, "wm": 3, "tap": 3}
    
    baths = int(input("Number of Combined Toilets (6 WSFU each): "))
    sinks = int(input("Number of Kitchen Sinks (2 WSFU each): "))
    wms = int(input("Number of Washing Machines (3 WSFU each): "))
    taps = int(input("Number of Outdoor Taps (3 WSFU each): "))
    
    wsfu_total = (baths * weights["bath"]) + (sinks * weights["sink"]) + \
                 (wms * weights["wm"]) + (taps * weights["tap"])
    
    print(f"Total Calculated WSFU: {wsfu_total}")

    # --- MODULE 4: HYDRAULIC BALANCING ---
    print("\n[4] Vertical Pipe Sizing (Gravity System)")
    # Hunter's Curve Approximation (Linearizing your 35 WSFU = 1.4 L/s report logic) [cite: 114]
    q_internal_ls = 1.4 * (wsfu_total / 35) 
    v_internal = 1.0 # Safe velocity to prevent noise/starvation [cite: 119]
    
    dia_internal_m = math.sqrt(((4 * (q_internal_ls/1000)) / (math.pi * v_internal))) [cite: 120]
    dia_internal_mm = dia_internal_m * 1000
    
    print(f"Peak Internal Flow: {q_internal_ls:.2f} L/s")
    print(f"Required Vertical Pipe Diameter: {dia_internal_mm:.2f} mm")

    # Commercial Selection Recommendation [cite: 121, 122, 124, 125]
    if dia_internal_mm <= 25:
        selection = "25mm (1\") UPVC"
    elif dia_internal_mm <= 32:
        selection = "32mm (1.25\") UPVC"
    elif dia_internal_mm <= 40:
        selection = "40mm (1.5\") UPVC"
    else:
        selection = "50mm (2\") UPVC"
        
    print(f"RECOMMENDED COMMERCIAL SIZE: {selection}")

if __name__ == "__main__":
    calculate_plumbing_system()
