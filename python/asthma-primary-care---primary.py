# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"4892","system":"med"},{"code":"16070","system":"med"},{"code":"39478","system":"med"},{"code":"3018","system":"med"},{"code":"663V1","system":"med"},{"code":"XE0YV","system":"med"},{"code":"XE0YX","system":"med"},{"code":"68C3.","system":"med"},{"code":"663V1","system":"med"},{"code":"H33zz","system":"med"},{"code":"XE0YX","system":"med"},{"code":"1J70.","system":"med"},{"code":"H35y7","system":"med"},{"code":"H33z0","system":"med"},{"code":"TJF7z","system":"med"},{"code":"XE0YV","system":"med"},{"code":"G581.11","system":"med"},{"code":"G581.","system":"med"},{"code":"3018","system":"med"},{"code":"4892","system":"med"},{"code":"39478","system":"med"},{"code":"16070","system":"med"},{"code":"XE0YV","system":"med"},{"code":"XE0YX","system":"med"},{"code":"663V1","system":"med"},{"code":"XE0YX","system":"med"},{"code":"H35y7","system":"med"},{"code":"H33zz","system":"med"},{"code":"XE0YV","system":"med"},{"code":"H33z0","system":"med"},{"code":"663V1","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-primary-care---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-primary-care---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-primary-care---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
