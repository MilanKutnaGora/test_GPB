def process_file(file_path):
    unique_records = {}
    duplicate_records = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        header = file.readline().strip().split('|')
        for line in file:
            record = line.strip().split('|')
            record_dict = dict(zip(header, record))
            id_value = record_dict['id']

            if id_value not in unique_records:
                unique_records[id_value] = record_dict
            else:
                if id_value not in duplicate_records:
                    duplicate_records[id_value] = [unique_records[id_value]]
                duplicate_records[id_value].append(record_dict)

    return unique_records, duplicate_records

# Пример использования
file_path = 'file.csv'
unique_records, duplicate_records = process_file(file_path)

print("Уникальные записи:")
for record in unique_records.values():
    print(', '.join(f"{key}={value}" for key, value in record.items()))

print("\nДубликаты записей:")
for id_value, records in duplicate_records.items():
    print(f"ID: {id_value}")
    for record in records:
        print(', '.join(f"{key}={value}" for key, value in record.items()))
    print()