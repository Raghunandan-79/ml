import numpy as np

def load_data(path):
    data = np.genfromtxt(path, delimiter=",", dtype=str, skip_header=1)
    print("Data loaded successfully!")
    return data

def extract_columns(data):
    distance = data[:, 0].astype(float)
    cab_type = data[:, 1] 

    price_col = data[:, 5]
    price_col[price_col == ""] = "nan"
    price = price_col.astype(float) 

    timestamp = data[:, 2].astype(float)

    return cab_type, distance, price, timestamp

def convert_to_hours(timestamp):
    hours = (timestamp // 3600) % 24
    return hours

def compute_basic_stats(distance):
    avg_dist = np.mean(distance)
    longest = np.max(distance)
    shortest = np.min(distance)
    return avg_dist, longest, shortest

def compare_prices(cab_type, price):
    uber_prices = price[cab_type == "Uber"]
    lyft_prices = price[cab_type == "Lyft"]

    avg_uber = np.mean(uber_prices) if len(uber_prices) else 0
    avg_lyft = np.mean(lyft_prices) if len(lyft_prices) else 0

    cheaper = "Uber" if avg_uber < avg_lyft else "Lyft"

    return avg_uber, avg_lyft, cheaper

def find_busiest_hour(hours):
    unique_hours, counts = np.unique(hours, return_counts=True)
    busiest_hour = unique_hours[np.argmax(counts)]
    return busiest_hour

def save_results(avg_dist, longest, shortest, avg_uber, avg_lyft, cheaper, busiest_hour):
    output = np.array([
        ["Metric", "Value"],
        ["Average Distance", avg_dist],
        ["Longest Trip", longest],
        ["Shortest Trip", shortest],
        ["Average Uber Price", avg_uber],
        ["Average Lyft Price", avg_lyft],
        ["Cheaper Service", cheaper],
        ["Busiest Hour", busiest_hour]
    ])

    np.savetxt("uber_analysis_output.csv", output, fmt="%s", delimiter=",")
    print("\nResults saved to uber_analysis_output.csv")

def main():
    path = input("Enter CSV file path: ")

    data = load_data(path)
    cab_type, distance, price, timestamp = extract_columns(data)

    hours = convert_to_hours(timestamp)

    avg_dist, longest, shortest = compute_basic_stats(distance)

    avg_uber, avg_lyft, cheaper = compare_prices(cab_type, price)

    busiest_hour = find_busiest_hour(hours)

    print("\n-------- RESULTS --------")
    print("Average Distance:", avg_dist)
    print("Longest Trip:", longest)
    print("Shortest Trip:", shortest)
    print("Average Uber Price:", avg_uber)
    print("Average Lyft Price:", avg_lyft)
    print("Cheaper On Average:", cheaper)
    print("Busiest Hour:", busiest_hour)

    save_results(avg_dist, longest, shortest, avg_uber, avg_lyft, cheaper, busiest_hour)


if __name__ == "__main__":
    main()