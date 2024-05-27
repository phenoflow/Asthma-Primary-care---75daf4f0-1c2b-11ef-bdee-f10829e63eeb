# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"19167","system":"med"},{"code":"25707","system":"med"},{"code":"25705","system":"med"},{"code":"25706","system":"med"},{"code":"11387","system":"med"},{"code":"41554","system":"med"},{"code":"81","system":"med"},{"code":"19539","system":"med"},{"code":"16655","system":"med"},{"code":"46529","system":"med"},{"code":"30382","system":"med"},{"code":"18141","system":"med"},{"code":"30458","system":"med"},{"code":"XaIu5","system":"med"},{"code":"9OJ4.","system":"med"},{"code":"XE2Nb","system":"med"},{"code":"XaBU3","system":"med"},{"code":"XaIu6","system":"med"},{"code":"XaIRN","system":"med"},{"code":"9OJ1.","system":"med"},{"code":"9OJ9.","system":"med"},{"code":"9OJ3.","system":"med"},{"code":"XaBU2","system":"med"},{"code":"9OJ9.","system":"med"},{"code":"9OJ1.","system":"med"},{"code":"9OJA.","system":"med"},{"code":"9OJ2.","system":"med"},{"code":"66YE.","system":"med"},{"code":"9OJ..","system":"med"},{"code":"9OJ5.","system":"med"},{"code":"66YR.","system":"med"},{"code":"9OJ4.","system":"med"},{"code":"9OJZ.","system":"med"},{"code":"9OJ6.","system":"med"},{"code":"663..","system":"med"},{"code":"9OJ3.","system":"med"},{"code":"66YQ.","system":"med"},{"code":"41554","system":"med"},{"code":"30382","system":"med"},{"code":"81","system":"med"},{"code":"25707","system":"med"},{"code":"46529","system":"med"},{"code":"18141","system":"med"},{"code":"11387","system":"med"},{"code":"19167","system":"med"},{"code":"25705","system":"med"},{"code":"30458","system":"med"},{"code":"19539","system":"med"},{"code":"25706","system":"med"},{"code":"XaIu5","system":"med"},{"code":"9OJ4.","system":"med"},{"code":"9OJ1.","system":"med"},{"code":"XaIu6","system":"med"},{"code":"XaBU2","system":"med"},{"code":"9OJ9.","system":"med"},{"code":"XaBU3","system":"med"},{"code":"9OJ3.","system":"med"},{"code":"XE2Nb","system":"med"},{"code":"XaIRN","system":"med"},{"code":"9OJ1.","system":"med"},{"code":"9OJ..","system":"med"},{"code":"66YQ.","system":"med"},{"code":"9OJA.","system":"med"},{"code":"66YR.","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma-primary-care-monitorng---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma-primary-care-monitorng---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma-primary-care-monitorng---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
