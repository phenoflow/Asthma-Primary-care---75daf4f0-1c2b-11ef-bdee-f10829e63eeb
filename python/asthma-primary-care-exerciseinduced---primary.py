# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"26506","system":"med"},{"code":"26504","system":"med"},{"code":"26861","system":"med"},{"code":"25181","system":"med"},{"code":"102871","system":"med"},{"code":"173A.","system":"med"},{"code":"663e.","system":"med"},{"code":"663e1","system":"med"},{"code":"663e0","system":"med"},{"code":"663f.","system":"med"},{"code":"XaObj","system":"med"},{"code":"178B.","system":"med"},{"code":"6635","system":"med"},{"code":"663e.","system":"med"},{"code":"25181","system":"med"},{"code":"26506","system":"med"},{"code":"26504","system":"med"},{"code":"26861","system":"med"},{"code":"102871","system":"med"},{"code":"663e0","system":"med"},{"code":"XaObj","system":"med"},{"code":"663e1","system":"med"},{"code":"663f.","system":"med"},{"code":"173A.","system":"med"},{"code":"663e.","system":"med"},{"code":"178B.","system":"med"},{"code":"663e.","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-primary-care-exerciseinduced---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-primary-care-exerciseinduced---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-primary-care-exerciseinduced---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
