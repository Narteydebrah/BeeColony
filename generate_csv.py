import random
import csv

n = 1000

with open('predicted_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['predicted_phasing', 'predicted_timing'])

    for i in range(n):
        # Generate realistic values for predicted_phasing and predicted_timing
        predicted_phasing = random.gauss(0.5, 0.1) + random.uniform(-0.2, 0.2)
        predicted_timing = random.gauss(0.5, 0.1) + random.uniform(-0.2, 0.2)

        writer.writerow([predicted_phasing, predicted_timing])

print('CSV file generated successfully.')
