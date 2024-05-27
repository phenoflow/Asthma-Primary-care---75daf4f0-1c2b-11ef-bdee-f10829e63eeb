# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"232","system":"med"},{"code":"8335","system":"med"},{"code":"XE0YW","system":"med"},{"code":"XE0ZT","system":"med"},{"code":"H33z1","system":"med"},{"code":"XE0ZT","system":"med"},{"code":"H33z1","system":"med"},{"code":"XM0s2","system":"med"},{"code":"XE0YW","system":"med"},{"code":"8335","system":"med"},{"code":"232","system":"med"},{"code":"H33z1","system":"med"},{"code":"XE0ZT","system":"med"},{"code":"XE0YW","system":"med"},{"code":"H33z1","system":"med"},{"code":"H33z111","system":"med"},{"code":"XE0ZT","system":"med"},{"code":"XE0YW","system":"med"},{"code":"XM0s2","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-primary-care-attack---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-primary-care-attack---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-primary-care-attack---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
