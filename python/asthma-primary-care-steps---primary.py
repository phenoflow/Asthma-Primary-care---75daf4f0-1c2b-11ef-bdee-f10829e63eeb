# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"29645","system":"med"},{"code":"20886","system":"med"},{"code":"18224","system":"med"},{"code":"20860","system":"med"},{"code":"16785","system":"med"},{"code":"16667","system":"med"},{"code":"18223","system":"med"},{"code":"9663","system":"med"},{"code":"Xa8Hn","system":"med"},{"code":"XaIQD","system":"med"},{"code":"8793.","system":"med"},{"code":"8796.","system":"med"},{"code":"8797.","system":"med"},{"code":"8794.","system":"med"},{"code":"XaIQE","system":"med"},{"code":"8798.","system":"med"},{"code":"8795.","system":"med"},{"code":"8796.","system":"med"},{"code":"8793.","system":"med"},{"code":"8794.","system":"med"},{"code":"8795.","system":"med"},{"code":"8798.","system":"med"},{"code":"8797.","system":"med"},{"code":"18224","system":"med"},{"code":"18223","system":"med"},{"code":"16785","system":"med"},{"code":"9663","system":"med"},{"code":"20860","system":"med"},{"code":"16667","system":"med"},{"code":"20886","system":"med"},{"code":"29645","system":"med"},{"code":"XaIQD","system":"med"},{"code":"8796.","system":"med"},{"code":"8795.","system":"med"},{"code":"8797.","system":"med"},{"code":"XaIQE","system":"med"},{"code":"8793.","system":"med"},{"code":"8794.","system":"med"},{"code":"Xa8Hn","system":"med"},{"code":"8798.","system":"med"},{"code":"8794.","system":"med"},{"code":"8793.","system":"med"},{"code":"8795.","system":"med"},{"code":"8797.","system":"med"},{"code":"8796.","system":"med"},{"code":"8798.","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-primary-care-steps---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-primary-care-steps---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-primary-care-steps---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
