import os
import csv
import json

# Task B1: OS Module checks
print("Checking file...")
if not os.path.exists('students.csv'):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()
print("File found: students.csv")

print("Checking output folder...")
if not os.path.exists('output'):
    os.makedirs('output')
    print("Output folder created: output/")
else:
    print("Output folder already exists: output/")


# Task B2: Read CSV and Preview Data
students = []
with open('students.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    students = list(reader)

print(f"Total students: {len(students)}")
print("First 5 rows:")
for s in students[:5]:
    print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

# Task B3: Country Analysis
country_counts = {}
for s in students:
    country = s['country']
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

print("\nStudents by Country")
for country, count in country_counts.items():
    print(f"{country}: {count}")

# Find top 3 using lambda
top_3_raw = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

print("\nTop 3 Countries:")
for rank, (country, count) in enumerate(top_3_raw, 1):
    print(f"{rank}. {country}: {count}")


# Task B4: Save Results to JSON and Print Summary
top_3_formatted = [{"country": c, "count": n} for c, n in top_3_raw]

result = {
    "analysis": "Country Analysis",
    "total_students": len(students),
    "total_countries": len(country_counts),
    "top_3_countries": top_3_formatted,
    "all_countries": country_counts
}

print("\nANALYSIS RESULT")
print("===============")
print(f"Analysis: {result['analysis']}")
print(f"Total students: {result['total_students']}")
print(f"Total countries: {result['total_countries']}")
print("Top 3 Countries:")
for i, item in enumerate(result['top_3_countries'], 1):
    print(f"{i}. {item['country']}: {item['count']}")
print("==============================")

with open('output/result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)

print("Result saved to output/result.json")
