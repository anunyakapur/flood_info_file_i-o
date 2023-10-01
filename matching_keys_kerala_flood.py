import csv

def create_kerala_districts(filename):
    
    kerala_flood_info = {}

    with open(filename, "r") as file_in:
        reader = csv.DictReader(file_in)

        for line in reader:
            district_name = line["district"]
            fatalities = int(line["fatalities"])
            no_of_camps = int(line["no_of_camps"])
            actual_rainfall_in_mm = float(line["actual_rainfall_in_mm"])
            normal_rainfall_in_mm = float(line["normal_rainfall_in_mm"])
            no_of_landslides = int(line["no_of_landslides"])
            full_damaged_houses = int(line["full_damaged_houses"])

            kerala_flood_info[district_name] = {"fatalities":fatalities, "num_camps": no_of_camps, "actual_rainfall_mm": actual_rainfall_in_mm, "normal_rainfall_mm": normal_rainfall_in_mm, 'no_landslides': no_of_landslides, "num_damaged_houses":full_damaged_houses, "warnings":[]}

    return kerala_flood_info
        
def add_kerala_flood_warnings(filename, kerala_flood_info):

    with open(filename, "r") as file_in:
        reader = csv.DictReader(file_in)

        for line in reader:
            district_name = line["district"]
            date = line["date"]
            actual_rainfall = line["actual_rainfall"]
            predicted_rainfall = line["predicted_rainfall"]

            entry = [date, actual_rainfall, predicted_rainfall]
            
            if kerala_flood_info[district_name]["warnings"] == []:
                kerala_flood_info[district_name]["warnings"] = entry
            else:
                kerala_flood_info[district_name]["warnings"].append(entry)

def print_kerala_flood_info(kerala_flood_info):
    for key in (kerala_flood_info):
        print(key)
        print(kerala_flood_info[key])

def main():
      flood_dict = create_kerala_districts("district_wise_details.csv")
      add_kerala_flood_warnings("warnings_actual_predicted.csv", flood_dict)

      print_kerala_flood_info(flood_dict)

main()
        
