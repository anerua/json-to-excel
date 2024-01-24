import json
import sys
import xlsxwriter

json_file = open(sys.argv[1])

deserialized_data = json.load(json_file)

# Create Excel workbook
workbook = xlsxwriter.Workbook(sys.argv[2])
# Add a worksheet
worksheet = workbook.add_worksheet()
 
# Add the column headers
headers = ("S/N", "Countries", "Continent", "Published Schools", "Schools Awaiting Revalidation", "Schools Under Review", "Rejected Schools",
           "Published Courses", "Published Courses (Bachelors)", "Published Courses (Masters)", "Published Courses (Doctorates)",
           "Courses Awaiting Revalidation", "Courses Awaiting Revalidation (Bachelors)", "Courses Awaiting Revalidation (Masters)", "Courses Awaiting Revalidation (Doctorates)",
           "Courses Under Review", "Courses Under Review (Bachelors)", "Courses Under Review (Masters)", "Courses Under Review (Doctorates)",
           "Rejected Courses", "Rejected Courses (Bachelors)", "Rejected Courses (Masters)", "Rejected Courses (Doctorates)",)
for i in range(len(headers)):
    worksheet.write(1, i+1, headers[i])

# Add json data
for i in range(len(deserialized_data)):
    row = i + 2
    worksheet.write(row, 1, i+1)
    col = 2
    entry = deserialized_data[i]
    for key in entry:
        worksheet.write(row, col, entry[key])
        col = col + 1

# Close the Excel file
workbook.close()