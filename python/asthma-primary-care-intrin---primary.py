# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"45073","system":"med"},{"code":"58196","system":"med"},{"code":"5267","system":"med"},{"code":"29325","system":"med"},{"code":"18323","system":"med"},{"code":"H331.","system":"med"},{"code":"H3310","system":"med"},{"code":"XE0YU","system":"med"},{"code":"X1022","system":"med"},{"code":"H3311","system":"med"},{"code":"H331z","system":"med"},{"code":"XE0ZR","system":"med"},{"code":"H3310","system":"med"},{"code":"XE0YU","system":"med"},{"code":"H331111","system":"med"},{"code":"H331.","system":"med"},{"code":"H3311","system":"med"},{"code":"H331z","system":"med"},{"code":"XE0ZR","system":"med"},{"code":"X1022","system":"med"},{"code":"45073","system":"med"},{"code":"29325","system":"med"},{"code":"18323","system":"med"},{"code":"5267","system":"med"},{"code":"58196","system":"med"},{"code":"X1022","system":"med"},{"code":"H331z","system":"med"},{"code":"XE0ZR","system":"med"},{"code":"H3310","system":"med"},{"code":"XE0YU","system":"med"},{"code":"H3311","system":"med"},{"code":"H331.","system":"med"},{"code":"H331.","system":"med"},{"code":"XE0ZR","system":"med"},{"code":"H331z","system":"med"},{"code":"H331111","system":"med"},{"code":"H3310","system":"med"},{"code":"XE0YU","system":"med"},{"code":"H3311","system":"med"},{"code":"X1022","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-primary-care-intrin---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-primary-care-intrin---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-primary-care-intrin---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
