# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"4741","system":"gprdproduct"},{"code":"4818","system":"gprdproduct"},{"code":"50185","system":"gprdproduct"},{"code":"51117","system":"gprdproduct"},{"code":"51519","system":"gprdproduct"},{"code":"51647","system":"gprdproduct"},{"code":"52208","system":"gprdproduct"},{"code":"52559","system":"gprdproduct"},{"code":"529","system":"gprdproduct"},{"code":"531","system":"gprdproduct"},{"code":"53680","system":"gprdproduct"},{"code":"53755","system":"gprdproduct"},{"code":"54326","system":"gprdproduct"},{"code":"54414","system":"gprdproduct"},{"code":"57026","system":"gprdproduct"},{"code":"57266","system":"gprdproduct"},{"code":"57273","system":"gprdproduct"},{"code":"57977","system":"gprdproduct"},{"code":"58646","system":"gprdproduct"},{"code":"59690","system":"gprdproduct"},{"code":"59802","system":"gprdproduct"},{"code":"7043","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('acei-loop-diuretic-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acei-loop-diuretic-m1-candesartan---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acei-loop-diuretic-m1-candesartan---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acei-loop-diuretic-m1-candesartan---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)