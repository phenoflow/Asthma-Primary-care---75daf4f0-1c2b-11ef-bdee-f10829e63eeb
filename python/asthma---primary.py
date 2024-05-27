# Luke Daines, Ann Morgan, Mome Mukherjee, Mohammad Al Sallakh, Eimear O'Rourke, Jennifer K Quint, 2024.

import sys, csv, re

codes = [{"code":"719","system":"med"},{"code":"78","system":"med"},{"code":"R96","system":"med"},{"code":"38B8.","system":"med"},{"code":"Y0017","system":"med"},{"code":"Y13a5","system":"med"},{"code":"Y13a4","system":"med"},{"code":"8791.","system":"med"},{"code":"H33z2","system":"med"},{"code":"Y137e","system":"med"},{"code":"663y.","system":"med"},{"code":"Y138a","system":"med"},{"code":"Y137f","system":"med"},{"code":"14B4.","system":"med"},{"code":"XM1Xb","system":"med"},{"code":"Y13a9","system":"med"},{"code":"Y139c","system":"med"},{"code":"663W.","system":"med"},{"code":"Y139d","system":"med"},{"code":"Y1b24","system":"med"},{"code":"H333.","system":"med"},{"code":"Y13a2","system":"med"},{"code":"Y1f90","system":"med"},{"code":"Y13a1","system":"med"},{"code":"Y139b","system":"med"},{"code":"Y13a8","system":"med"},{"code":"Y13a7","system":"med"},{"code":"Y13a3","system":"med"},{"code":"H33..","system":"med"},{"code":"XM0s2","system":"med"},{"code":"XaINg","system":"med"},{"code":"XaIIY","system":"med"},{"code":"XaRFi","system":"med"},{"code":"XaObl","system":"med"},{"code":"XaIeq","system":"med"},{"code":"XaX3n","system":"med"},{"code":"XaObm","system":"med"},{"code":"XaJFG","system":"med"},{"code":"XaXZx","system":"med"},{"code":"XaIfK","system":"med"},{"code":"XaIoE","system":"med"},{"code":"XaLJT","system":"med"},{"code":"XaNKw","system":"med"},{"code":"XaXa0","system":"med"},{"code":"XaXZs","system":"med"},{"code":"XaRFk","system":"med"},{"code":"X1025","system":"med"},{"code":"XaLIn","system":"med"},{"code":"XaINZ","system":"med"},{"code":"XaObi","system":"med"},{"code":"XaRFl","system":"med"},{"code":"XaINf","system":"med"},{"code":"XaXZm","system":"med"},{"code":"XaRFj","system":"med"},{"code":"XaXZp","system":"med"},{"code":"XaIIZ","system":"med"},{"code":"XaQHq","system":"med"},{"code":"XaIIW","system":"med"},{"code":"XaQig","system":"med"},{"code":"XaIQ4","system":"med"},{"code":"XaLIm","system":"med"},{"code":"XaObj","system":"med"},{"code":"14B4.","system":"med"},{"code":"XaYZh","system":"med"},{"code":"H33..","system":"med"},{"code":"XaIuG","system":"med"},{"code":"XaINd","system":"med"},{"code":"XaY2V","system":"med"},{"code":"XaXZu","system":"med"},{"code":"XaINa","system":"med"},{"code":"XaLJS","system":"med"},{"code":"XaINc","system":"med"},{"code":"XaObk","system":"med"},{"code":"XaQih","system":"med"},{"code":"XaYb8","system":"med"},{"code":"XaLJU","system":"med"},{"code":"XaLIr","system":"med"},{"code":"XaDvK","system":"med"},{"code":"XaYZB","system":"med"},{"code":"XaINh","system":"med"},{"code":"XaIIX","system":"med"},{"code":"XaIR3","system":"med"},{"code":"XaINb","system":"med"},{"code":"719","system":"med"},{"code":"78","system":"med"},{"code":"Y139c","system":"med"},{"code":"Y13a2","system":"med"},{"code":"38B8.","system":"med"},{"code":"Y1b24","system":"med"},{"code":"Y13a7","system":"med"},{"code":"Y0017","system":"med"},{"code":"H33..","system":"med"},{"code":"H33z2","system":"med"},{"code":"Y13a5","system":"med"},{"code":"Y13a3","system":"med"},{"code":"14B4.","system":"med"},{"code":"XM0s2","system":"med"},{"code":"Y137f","system":"med"},{"code":"XM1Xb","system":"med"},{"code":"8791.","system":"med"},{"code":"H333.","system":"med"},{"code":"663y.","system":"med"},{"code":"Y139d","system":"med"},{"code":"Y13a8","system":"med"},{"code":"Y1f90","system":"med"},{"code":"Y138a","system":"med"},{"code":"Y13a4","system":"med"},{"code":"Y13a1","system":"med"},{"code":"Y137e","system":"med"},{"code":"Y13a9","system":"med"},{"code":"Y139b","system":"med"},{"code":"663W.","system":"med"},{"code":"H33..","system":"med"},{"code":"14B4.","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
