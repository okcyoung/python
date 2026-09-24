"""
Name: Yang Zhu
Student ID: [24333941]
Description: CITS1401 Lab04 - Statistical analysis of global organisations.
This program reads a CSV file dynamically, computes standard deviations and 
Pearson correlation coefficients without using any external modules, 
and gracefully handles errors.
"""

def get_column_indices(headers):
    
    indices = {
        'name': -1,
        'country': -1,
        'employees': -1,
        'salary': -1,
        'profit_2020': -1,
        'profit_2021': -1
    }
    
   
    for i in range(len(headers)):
        
        
        header = headers[i].lower()
                
        if "name" in header and "country" not in header:
            indices['name'] = i
            
        elif "country" in header:
            indices['country'] = i
            
        elif "employee" in header:
            indices['employees'] = i
            
        elif "salary" in header:
            indices['salary'] = i
            
        elif "2020" in header:
            indices['profit_2020'] = i
            
        elif "2021" in header:
            indices['profit_2021'] = i
            
    return indices

def calc_mean(data_list):
    """Calculates the arithmetic mean of a list of numbers."""
    if not data_list:
        return 0.0
    return sum(data_list) / len(data_list)

def calc_sample_std_dev(data_list):
    """Calculates the sample standard deviation (N-1) using pure math."""
    n = len(data_list)
    if n < 2:
        return 0.0  # Mathematically undefined for N < 2
        
    mean_val = calc_mean(data_list)
    variance_sum = sum((x - mean_val) ** 2 for x in data_list)
    return (variance_sum / (n - 1)) ** 0.5

def calc_pearson_correlation(x_data, y_data):
    """Calculates the Pearson correlation coefficient."""
    n = len(x_data)
    if n == 0 or n != len(y_data):
        return -2  # Error state or empty data
        
    mean_x = calc_mean(x_data)
    mean_y = calc_mean(y_data)
    
    numerator = sum((x_data[i] - mean_x) * (y_data[i] - mean_y) for i in range(n))
    sum_sq_x = sum((x_data[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y_data[i] - mean_y) ** 2 for i in range(n))
    
    denominator = (sum_sq_x ** 0.5) * (sum_sq_y ** 0.5)
    
    if denominator == 0:
        return -2  # Prevent division by zero
        
    return numerator / denominator



def main(csvfile, country):
    """
    Main entry point of the program.
    Reads the CSV, processes line by line, and calculates outputs.
    """
    target_country = country.strip().lower()
    
    # OP1 Variables
    max_profit_change = float('-inf')
    min_profit_change = float('inf')
    org_max_change = ""
    org_min_change = ""
    
    # OP2 Variables
    country_profits_2021 = []
    all_profits_2021 = []
    
    # OP3 Variables
    x_salaries = []
    y_profit_changes = []
    
    try:
        # Gracefully handle file opening
        with open(csvfile, 'r', encoding='utf-8') as file:
            header_line = file.readline()
            if not header_line:
                return ([], [], -2)  # Empty file error state
                
            headers = header_line.strip().split(',')
            indices = get_column_indices(headers)
            
            # Check if any required column is missing
            if -1 in indices.values():
                return ([], [], -2) 
                
            # Iterate through the file line by line (Efficient Memory Management)
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                row = line.split(',')
                
                # Protect against malformed rows
                if len(row) <= max(indices.values()):
                    continue
                    
                try:
                    # Data Extraction
                    org_name = row[indices['name']]
                    org_country = row[indices['country']].lower()
                    employees = float(row[indices['employees']])
                    salary = float(row[indices['salary']])
                    profit_2020 = float(row[indices['profit_2020']])
                    profit_2021 = float(row[indices['profit_2021']])
                except ValueError:
                    # Skip row if numeric conversion fails 
                    continue
                    
                profit_change = profit_2021 - profit_2020
                
                # Global Task (OP2)
                all_profits_2021.append(profit_2021)
                
                # Country Specific Tasks
                if org_country == target_country:
                    
                    # OP1: Track Max and Min Profit Change
                    if profit_change > max_profit_change:
                        max_profit_change = profit_change
                        org_max_change = org_name
                        
                    if profit_change < min_profit_change:
                        min_profit_change = profit_change
                        org_min_change = org_name
                        
                    # OP2: Collect country specific 2021 profits
                    country_profits_2021.append(profit_2021)
                    
                    # OP3: Collect data for Pearson correlation (Rules: change > 0 AND emp > 5000)
                    if profit_change > 0 and employees > 5000:
                        x_salaries.append(salary)
                        y_profit_changes.append(profit_change)
                        
    except (FileNotFoundError, IOError):
        # Graceful exit for file-level errors
        return ([], [], -2)
    except Exception:
        # Catch any unexpected catastrophic failure
        return ([], [], -2)

    # --- Final Output Formatting ---
    
    # OP1 Format
    OP1 = []
    if org_max_change and org_min_change:
        OP1 = [org_max_change, org_min_change]
        
    # OP2 Format
    OP2 = []
    if all_profits_2021:
        std_country = calc_sample_std_dev(country_profits_2021)
        std_all = calc_sample_std_dev(all_profits_2021)
        OP2 = [round(std_country, 4), round(std_all, 4)]
    else:
        # If the file had valid headers but absolutely no data rows
        return ([], [], -2)
        
    # OP3 Format
    OP3 = calc_pearson_correlation(x_salaries, y_profit_changes)
    if OP3 != -2:
        OP3 = round(OP3, 4)
        
    return OP1, OP2, OP3