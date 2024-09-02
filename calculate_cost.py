# Function to calculate percentage change between two values
def calculate_percentage_change(old_value, new_value):
    return ((new_value - old_value) / old_value) * 100
# Formatting large numbers for display
def format_number(number):
    if number >= 1_000_000:
        return f"{number/1_000_000:.4f} million"
    else:
        return f"{number}"
# Function to calculate cost based on consumption units and period
def calculate_househhold_cost(units, period_key):
    breakdown = []
    total_cost = 0

    if period_key == "period_1": 
        if units <= 100:
            total_cost = units * 35
            breakdown.append(f"{units} units x 35 MMK = {format_number(total_cost)} MMK")
        elif units <= 200:
            total_cost = 100 * 35 + (units - 100) * 40
            breakdown.append("100 units x 35 MMK = 3,500 MMK")
            breakdown.append(f"{units - 100} units x 40 MMK = {format_number((units - 100) * 40)} MMK")
        else:
            total_cost = 100 * 35 + 100 * 40 + (units - 200) * 50
            breakdown.append("100 units x 35 MMK = 3,500 MMK")
            breakdown.append("100 units x 40 MMK = 4,000 MMK")
            breakdown.append(f"{units - 200} units x 50 MMK = {format_number((units - 200) * 50)} MMK")

    elif period_key == "period_2":
        if units <= 30:
            total_cost = units * 35
            breakdown.append(f"{units} units x 35 MMK = {format_number(total_cost)} MMK")
        elif units <= 50:
            total_cost = 30 * 35 + (units - 30) * 50
            breakdown.append("30 units x 35 MMK = 1,050 MMK")
            breakdown.append(f"{units - 30} units x 50 MMK = {format_number((units - 30) * 50)} MMK")
        elif units <= 75:
            total_cost = 30 * 35 + 20 * 50 + (units - 50) * 70
            breakdown.append("30 units x 35 MMK = 1,050 MMK")
            breakdown.append("20 units x 50 MMK = 1,000 MMK")
            breakdown.append(f"{units - 50} units x 70 MMK = {format_number((units - 50) * 70)} MMK")
        elif units <= 100:
            total_cost = 30 * 35 + 20 * 50 + 25 * 70 + (units - 75) * 90
            breakdown.append("30 units x 35 MMK = 1,050 MMK")
            breakdown.append("20 units x 50 MMK = 1,000 MMK")
            breakdown.append("25 units x 70 MMK = 1,750 MMK")
            breakdown.append(f"{units - 75} units x 90 MMK = {format_number((units - 75) * 90)} MMK")
        elif units <= 150:
            total_cost = 30 * 35 + 20 * 50 + 25 * 70 + 25 * 90 + (units - 100) * 110
            breakdown.append("30 units x 35 MMK = 1,050 MMK")
            breakdown.append("20 units x 50 MMK = 1,000 MMK")
            breakdown.append("25 units x 70 MMK = 1,750 MMK")
            breakdown.append("25 units x 90 MMK = 2,250 MMK")
            breakdown.append(f"{units - 100} units x 110 MMK = {format_number((units - 100) * 110)} MMK")
        elif units <= 200:
            total_cost = 30 * 35 + 20 * 50 + 25 * 70 + 25 * 90 + 50 * 110 + (units - 150) * 120
            breakdown.append("30 units x 35 MMK = 1,050 MMK")
            breakdown.append("20 units x 50 MMK = 1,000 MMK")
            breakdown.append("25 units x 70 MMK = 1,750 MMK")
            breakdown.append("25 units x 90 MMK = 2,250 MMK")
            breakdown.append("50 units x 110 MMK = 5,500 MMK")
            breakdown.append(f"{units - 150} units x 120 MMK = {format_number((units - 150) * 120)} MMK")
        else:
            total_cost = 30 * 35 + 20 * 50 + 25 * 70 + 25 * 90 + 50 * 110 + 50 * 120 + (units - 200) * 125
            breakdown.append("30 units x 35 MMK = 1,050 MMK")
            breakdown.append("20 units x 50 MMK = 1,000 MMK")
            breakdown.append("25 units x 70 MMK = 1,750 MMK")
            breakdown.append("25 units x 90 MMK = 2,250 MMK")
            breakdown.append("50 units x 110 MMK = 5,500 MMK")
            breakdown.append("50 units x 120 MMK = 6,000 MMK")
            breakdown.append(f"{units - 200} units x 125 MMK = {format_number((units - 200) * 125)} MMK")

    elif period_key == "period_3":  # Starting September 2024
        if units <= 50:
            total_cost = units * 50
            breakdown.append(f"{units} units x 50 MMK = {format_number(total_cost)} MMK")
        elif units <= 100:
            total_cost = 50 * 50 + (units - 50) * 100
            breakdown.append("50 units x 50 MMK = 2,500 MMK")
            breakdown.append(f"{units - 50} units x 100 MMK = {format_number((units - 50) * 100)} MMK")
        elif units <= 200:
            total_cost = 50 * 50 + 50 * 100 + (units - 100) * 150
            breakdown.append("50 units x 50 MMK = 2,500 MMK")
            breakdown.append("50 units x 100 MMK = 5,000 MMK")
            breakdown.append(f"{units - 100} units x 150 MMK = {format_number((units - 100) * 150)} MMK")
        else:
            total_cost = 50 * 50 + 50 * 100 + 100 * 150 + (units - 200) * 300
            breakdown.append("50 units x 50 MMK = 2,500 MMK")
            breakdown.append("50 units x 100 MMK = 5,000 MMK")
            breakdown.append("100 units x 150 MMK = 15,000 MMK")
            breakdown.append(f"{units - 200} units x 300 MMK = {format_number((units - 200) * 300)} MMK")

    return total_cost, breakdown


def calculate_industrial_cost(units, period_key):
    breakdown = []
    total_cost = 0

    if period_key == "period_1":  # Before 2019
        if units <= 500:
            total_cost = units * 75
            breakdown.append(f"{units} units x 75 MMK = {format_number(total_cost)} MMK")
        elif units <= 5000:
            total_cost = 500 * 75 + (units - 500) * 100
            breakdown.append("500 units x 75 MMK = 37,500 MMK")
            breakdown.append(f"{units - 500} units x 100 MMK = {format_number((units - 500) * 100)} MMK")
        elif units <= 10000:
            total_cost = 500 * 75 + 4500 * 100 + (units - 5000) * 100
            breakdown.append("500 units x 75 MMK = 37,500 MMK")
            breakdown.append("4500 units x 100 MMK = 450,000 MMK")
            breakdown.append(f"{units - 5000} units x 100 MMK = {format_number((units - 5000) * 100)} MMK")
        # Continue similarly for other ranges...

    elif period_key == "period_2":  # 2019 to 2024
        if units <= 500:
            total_cost = units * 125
            breakdown.append(f"{units} units x 125 MMK = {format_number(total_cost)} MMK")
        elif units <= 5000:
            total_cost = 500 * 125 + (units - 500) * 135
            breakdown.append("500 units x 125 MMK = 62,500 MMK")
            breakdown.append(f"{units - 500} units x 135 MMK = {format_number((units - 500) * 135)} MMK")
        elif units <= 10000:
            total_cost = 500 * 125 + 4500 * 135 + (units - 5000) * 145
            breakdown.append("500 units x 125 MMK = 62,500 MMK")
            breakdown.append("4500 units x 135 MMK = 607,500 MMK")
            breakdown.append(f"{units - 5000} units x 145 MMK = {format_number((units - 5000) * 145)} MMK")
        # Continue similarly for other ranges...

    elif period_key == "period_3":  # 2024 New Rate
        if units <= 5000:
            total_cost = units * 250
            breakdown.append(f"{units} units x 250 MMK = {format_number(total_cost)} MMK")
        elif units <= 20000:
            total_cost = 5000 * 250 + (units - 5000) * 400
            breakdown.append("5000 units x 250 MMK = 1,250,000 MMK")
            breakdown.append(f"{units - 5000} units x 400 MMK = {format_number((units - 5000) * 400)} MMK")
        elif units > 20000:
            total_cost = 5000 * 250 + 15000 * 400 + (units - 20000) * 500
            breakdown.append("5000 units x 250 MMK = 1,250,000 MMK")
            breakdown.append("15000 units x 400 MMK = 6,000,000 MMK")
            breakdown.append(f"{units - 20000} units x 500 MMK = {format_number((units - 20000) * 500)} MMK")

    return total_cost, breakdown
