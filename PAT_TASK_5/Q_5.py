from datetime import datetime

# date_time = datetime.now()
# print(date_time)

date = datetime(2026, 1, 1)        #object
extract_date = lambda x: (x.year, x.month, x.day)
final = extract_date(date)       #extracting the data from the object
print(final)

