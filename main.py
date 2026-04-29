import os
import csv
import json

# # Task B1: OS Module checks
# print("Checking file...")
# if not os.path.exists('students.csv'):
#     print("Error: students.csv not found. Please download the file from LMS.")
#     exit()
# print("File found: students.csv")

# print("Checking output folder...")
# if not os.path.exists('output'):
#     os.makedirs('output')
#     print("Output folder created: output/")
# else:
#     print("Output folder already exists: output/")


# # Task B2: Read CSV and Preview Data
# students = []
# with open('students.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     students = list(reader)

# print(f"Total students: {len(students)}")
# print("First 5 rows:")
# for s in students[:5]:
#     print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

# # Task B3: Country Analysis
# country_counts = {}
# for s in students:
#     country = s['country']
#     if country in country_counts:
#         country_counts[country] += 1
#     else:
#         country_counts[country] = 1

# print("\nStudents by Country")
# for country, count in country_counts.items():
#     print(f"{country}: {count}")

# # Find top 3 using lambda
# top_3_raw = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

# print("\nTop 3 Countries:")
# for rank, (country, count) in enumerate(top_3_raw, 1):
#     print(f"{rank}. {country}: {count}")


# # Task B4: Save Results to JSON and Print Summary
# top_3_formatted = [{"country": c, "count": n} for c, n in top_3_raw]

# result = {
#     "analysis": "Country Analysis",
#     "total_students": len(students),
#     "total_countries": len(country_counts),
#     "top_3_countries": top_3_formatted,
#     "all_countries": country_counts
# }

# print("\nANALYSIS RESULT")
# print("===============")
# print(f"Analysis: {result['analysis']}")
# print(f"Total students: {result['total_students']}")
# print(f"Total countries: {result['total_countries']}")
# print("Top 3 Countries:")
# for i, item in enumerate(result['top_3_countries'], 1):
#     print(f"{i}. {item['country']}: {item['count']}")
# print("==============================")

# with open('output/result.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, indent=4)

# print("Result saved to output/result.json")

# #assignment 2:
# #b1
# def check_files():
#     """Проверяет наличие файла данных и создает папку для вывода."""
#     print("Checking file...")
#     file_exists = os.path.exists('students.csv')
    
#     if file_exists:
#         print("File found: students.csv")
#     else:
#         print("Error: students.csv not found")
#         return False

#     print("Checking output folder...")
#     if not os.path.exists('output'):
#         os.makedirs('output')
#         print("Output folder created: output/")
#     else:
#         print("Output folder already exists: output/")
    
#     return file_exists

# def load_data(filename):
#     """Загружает данные из CSV и возвращает список словарей."""
#     print("Loading data...")
#     with open(filename, mode='r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         return list(reader)

# def preview_data(students, n=5):
#     """Выводит первые n строк данных (по умолчанию 5)."""
#     print(f"First {n} rows:")
#     for s in students[:n]:
#         print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']}| GPA: {s['GPA']}[cite: 2]")

# #b2
# def analyse_countries(students):
#     """Анализирует распределение студентов по странам[cite: 2]."""
#     country_counts = {}
    
#     for s in students:
#         try:
#             # Обработка исключений при конвертации, если бы мы считали числа[cite: 2]
#             country = s['country']
#             country_counts[country] = country_counts.get(country, 0) + 1
#         except Exception as e:
#             print(f"Warning: could not process row for student {s.get('student_id')}. Skipping.[cite: 2]")
#             continue

#     # Поиск ТОП-3 через lambda[cite: 2]
#     top_3_list = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
#     top_3_formatted = [{"country": c, "count": count} for c, count in top_3_list]

#     return {
#         "total_students": len(students),
#         "total_countries": len(country_counts),
#         "top_3": top_3_formatted,
#         "all_countries": country_counts
#     }

# #b3
# def run_advanced_processing(students):
#     """Демонстрация использования lambda, map и filter[cite: 2]."""
#     print("\nLambda / Map / Filter")
    
#     # 1Фильтр: студенты с GPA > 3.5[cite: 2]
#     high_gpa = list(filter(lambda s: float(s['GPA']) > 3.5, students))
#     print(f"GPA > 3.5: {len(high_gpa)}[cite: 2]")
    
#     # 2.Map: извлечение только значений GPA[cite: 2]
#     gpa_values = list(map(lambda s: float(s['GPA']), students))
#     print(f"GPA values (first 5): {gpa_values[:5]}[cite: 2]")
    
#     # 3.Фильтр: посещаемость > 90%[cite: 2]
#     good_attendance = list(filter(lambda s: float(s['class_attendance_percent']) > 90, students))
#     print(f"class_attendance_percent > 90: {len(good_attendance)}[cite: 2]")

# #b4

# # Основной запуск программы
# if __name__ == "__main__":
#     if check_files():
#         try:
#             # Попытка загрузки данных с обработкой FileNotFoundError[cite: 2]
#             data = load_data('students.csv')
#             preview_data(data)
            
#             # Анализ
#             results = analyse_countries(data)
            
#             print("\nCountry Analysis")
#             print(f"Total countries: {results['total_countries']}[cite: 2]")
#             print("Top 3 Countries:")
#             for i, item in enumerate(results['top_3'], 1):
#                 print(f"{i}. {item['country']}: {item['count']}[cite: 2]")
            
#             # Продвинутая обработка
#             run_advanced_processing(data)
            
#             # Тест обработки ошибок (несуществующий файл)[cite: 2]
#             print("\nTesting error handling...")
#             try:
#                 wrong_data = load_data("wrong_file.csv")
#             except FileNotFoundError:
#                 print("Error: File 'wrong_file.csv' not found. Please check the filename.[cite: 2]")
                
#         except Exception as e:
#             print(f"General error: {e}[cite: 2]")


class FileManager:
    """Task 1: Управление файлами и папками."""
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        print(f"Error: {self.filename} not found")
        return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

class DataLoader:
    """Task 2: Загрузка и предварительный просмотр данных."""
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                self.students = list(csv.DictReader(f))
            print(f"Data loaded successfully: {len(self.students)} students[cite: 1]")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found[cite: 1]")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:[cite: 1]")
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}[cite: 1]")

class DataAnalyser:
    """Task 3 (Variant B): Анализ стран[cite: 1]."""
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        """Логика анализа для Варианта B[cite: 1]."""
        country_counts = {}
        for s in self.students:
            try:
                c = s['country']
                country_counts[c] = country_counts.get(c, 0) + 1
            except KeyError:
                continue

        # Сортировка ТОП-3 через lambda[cite: 1]
        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        
        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3_countries": [{"country": k, "count": v} for k, v in top_3],
            "all_countries": country_counts
        }
        return self.result

    def print_results(self):
        print("\nCountry Analysis[cite: 1]")
        print(f"Total countries: {self.result['total_countries']}[cite: 1]")
        print("Top 3 Countries:[cite: 1]")
        for i, item in enumerate(self.result['top_3_countries'], 1):
            print(f"{i}. {item['country']}: {item['count']}[cite: 1]")

class ResultSaver:
    """Task 4: Сохранение результатов в JSON[cite: 1]."""
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}[cite: 1]")
        except Exception as e:
            print(f"Error saving file: {e}[cite: 1]")

# Task 5: Главная логика программы[cite: 1]
if __name__ == "__main__":
    # Инициализация объектов
    fm = FileManager('students.csv')
    
    # 1. Проверка файла
    if not fm.check_file():
        print("Stopping program.[cite: 1]")
        exit()
    
    fm.create_output_folder()

    # 2. Загрузка данных
    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    # 3. Анализ (Вариант B)
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    # 4. Сохранение
    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()