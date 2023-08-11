# S Jill Stocks, Evangelos Kontopantelis, Artur Akbarov, Sarah Rodgers, Anthony J Avery, Darren M Aschroft, 2023.

import sys, csv, re

codes = [{"code":"10066","system":"gprdproduct"},{"code":"10323","system":"gprdproduct"},{"code":"10882","system":"gprdproduct"},{"code":"10902","system":"gprdproduct"},{"code":"11133","system":"gprdproduct"},{"code":"11197","system":"gprdproduct"},{"code":"11268","system":"gprdproduct"},{"code":"11351","system":"gprdproduct"},{"code":"1143","system":"gprdproduct"},{"code":"1144","system":"gprdproduct"},{"code":"11487","system":"gprdproduct"},{"code":"11561","system":"gprdproduct"},{"code":"11567","system":"gprdproduct"},{"code":"11641","system":"gprdproduct"},{"code":"11937","system":"gprdproduct"},{"code":"11965","system":"gprdproduct"},{"code":"11987","system":"gprdproduct"},{"code":"12294","system":"gprdproduct"},{"code":"12412","system":"gprdproduct"},{"code":"13026","system":"gprdproduct"},{"code":"1369","system":"gprdproduct"},{"code":"14283","system":"gprdproduct"},{"code":"14387","system":"gprdproduct"},{"code":"14587","system":"gprdproduct"},{"code":"15135","system":"gprdproduct"},{"code":"1520","system":"gprdproduct"},{"code":"16196","system":"gprdproduct"},{"code":"16197","system":"gprdproduct"},{"code":"16924","system":"gprdproduct"},{"code":"17006","system":"gprdproduct"},{"code":"17474","system":"gprdproduct"},{"code":"17624","system":"gprdproduct"},{"code":"18263","system":"gprdproduct"},{"code":"19204","system":"gprdproduct"},{"code":"196","system":"gprdproduct"},{"code":"20188","system":"gprdproduct"},{"code":"211","system":"gprdproduct"},{"code":"21162","system":"gprdproduct"},{"code":"21423","system":"gprdproduct"},{"code":"21938","system":"gprdproduct"},{"code":"22708","system":"gprdproduct"},{"code":"23456","system":"gprdproduct"},{"code":"24632","system":"gprdproduct"},{"code":"2493","system":"gprdproduct"},{"code":"25382","system":"gprdproduct"},{"code":"26995","system":"gprdproduct"},{"code":"277","system":"gprdproduct"},{"code":"2772","system":"gprdproduct"},{"code":"28127","system":"gprdproduct"},{"code":"28129","system":"gprdproduct"},{"code":"28438","system":"gprdproduct"},{"code":"28486","system":"gprdproduct"},{"code":"28586","system":"gprdproduct"},{"code":"28820","system":"gprdproduct"},{"code":"29530","system":"gprdproduct"},{"code":"29627","system":"gprdproduct"},{"code":"30039","system":"gprdproduct"},{"code":"3069","system":"gprdproduct"},{"code":"30773","system":"gprdproduct"},{"code":"30921","system":"gprdproduct"},{"code":"31773","system":"gprdproduct"},{"code":"32166","system":"gprdproduct"},{"code":"33057","system":"gprdproduct"},{"code":"33336","system":"gprdproduct"},{"code":"33527","system":"gprdproduct"},{"code":"33658","system":"gprdproduct"},{"code":"33811","system":"gprdproduct"},{"code":"34382","system":"gprdproduct"},{"code":"34390","system":"gprdproduct"},{"code":"34400","system":"gprdproduct"},{"code":"34412","system":"gprdproduct"},{"code":"34429","system":"gprdproduct"},{"code":"34431","system":"gprdproduct"},{"code":"34432","system":"gprdproduct"},{"code":"34471","system":"gprdproduct"},{"code":"34490","system":"gprdproduct"},{"code":"34505","system":"gprdproduct"},{"code":"34528","system":"gprdproduct"},{"code":"34539","system":"gprdproduct"},{"code":"34540","system":"gprdproduct"},{"code":"34562","system":"gprdproduct"},{"code":"34567","system":"gprdproduct"},{"code":"34589","system":"gprdproduct"},{"code":"34613","system":"gprdproduct"},{"code":"34652","system":"gprdproduct"},{"code":"34732","system":"gprdproduct"},{"code":"34936","system":"gprdproduct"},{"code":"35173","system":"gprdproduct"},{"code":"35174","system":"gprdproduct"},{"code":"35196","system":"gprdproduct"},{"code":"35317","system":"gprdproduct"},{"code":"35329","system":"gprdproduct"},{"code":"35343","system":"gprdproduct"},{"code":"35481","system":"gprdproduct"},{"code":"35697","system":"gprdproduct"},{"code":"35794","system":"gprdproduct"},{"code":"36190","system":"gprdproduct"},{"code":"37080","system":"gprdproduct"},{"code":"37087","system":"gprdproduct"},{"code":"3720","system":"gprdproduct"},{"code":"37655","system":"gprdproduct"},{"code":"37778","system":"gprdproduct"},{"code":"37908","system":"gprdproduct"},{"code":"37930","system":"gprdproduct"},{"code":"37964","system":"gprdproduct"},{"code":"37965","system":"gprdproduct"},{"code":"37978","system":"gprdproduct"},{"code":"38034","system":"gprdproduct"},{"code":"38308","system":"gprdproduct"},{"code":"38459","system":"gprdproduct"},{"code":"38889","system":"gprdproduct"},{"code":"39227","system":"gprdproduct"},{"code":"39512","system":"gprdproduct"},{"code":"39807","system":"gprdproduct"},{"code":"40355","system":"gprdproduct"},{"code":"40639","system":"gprdproduct"},{"code":"40711","system":"gprdproduct"},{"code":"40898","system":"gprdproduct"},{"code":"41205","system":"gprdproduct"},{"code":"41232","system":"gprdproduct"},{"code":"41417","system":"gprdproduct"},{"code":"41532","system":"gprdproduct"},{"code":"41538","system":"gprdproduct"},{"code":"41617","system":"gprdproduct"},{"code":"41694","system":"gprdproduct"},{"code":"41719","system":"gprdproduct"},{"code":"4182","system":"gprdproduct"},{"code":"4226","system":"gprdproduct"},{"code":"42901","system":"gprdproduct"},{"code":"42908","system":"gprdproduct"},{"code":"43411","system":"gprdproduct"},{"code":"43412","system":"gprdproduct"},{"code":"43418","system":"gprdproduct"},{"code":"43432","system":"gprdproduct"},{"code":"43507","system":"gprdproduct"},{"code":"43508","system":"gprdproduct"},{"code":"43563","system":"gprdproduct"},{"code":"43566","system":"gprdproduct"},{"code":"43649","system":"gprdproduct"},{"code":"44527","system":"gprdproduct"},{"code":"44657","system":"gprdproduct"},{"code":"448","system":"gprdproduct"},{"code":"45217","system":"gprdproduct"},{"code":"45337","system":"gprdproduct"},{"code":"45554","system":"gprdproduct"},{"code":"45816","system":"gprdproduct"},{"code":"46525","system":"gprdproduct"},{"code":"46792","system":"gprdproduct"},{"code":"46851","system":"gprdproduct"},{"code":"46890","system":"gprdproduct"},{"code":"46974","system":"gprdproduct"},{"code":"46975","system":"gprdproduct"},{"code":"47021","system":"gprdproduct"},{"code":"47467","system":"gprdproduct"},{"code":"47573","system":"gprdproduct"},{"code":"47727","system":"gprdproduct"},{"code":"47998","system":"gprdproduct"},{"code":"48008","system":"gprdproduct"},{"code":"48053","system":"gprdproduct"},{"code":"48398","system":"gprdproduct"},{"code":"4873","system":"gprdproduct"},{"code":"49492","system":"gprdproduct"},{"code":"50347","system":"gprdproduct"},{"code":"50607","system":"gprdproduct"},{"code":"50863","system":"gprdproduct"},{"code":"50971","system":"gprdproduct"},{"code":"51186","system":"gprdproduct"},{"code":"51701","system":"gprdproduct"},{"code":"51714","system":"gprdproduct"},{"code":"51807","system":"gprdproduct"},{"code":"51983","system":"gprdproduct"},{"code":"520","system":"gprdproduct"},{"code":"52088","system":"gprdproduct"},{"code":"52189","system":"gprdproduct"},{"code":"52197","system":"gprdproduct"},{"code":"52499","system":"gprdproduct"},{"code":"5275","system":"gprdproduct"},{"code":"52882","system":"gprdproduct"},{"code":"53220","system":"gprdproduct"},{"code":"53621","system":"gprdproduct"},{"code":"53820","system":"gprdproduct"},{"code":"53915","system":"gprdproduct"},{"code":"54283","system":"gprdproduct"},{"code":"54298","system":"gprdproduct"},{"code":"54544","system":"gprdproduct"},{"code":"54620","system":"gprdproduct"},{"code":"54740","system":"gprdproduct"},{"code":"54941","system":"gprdproduct"},{"code":"55358","system":"gprdproduct"},{"code":"55456","system":"gprdproduct"},{"code":"55718","system":"gprdproduct"},{"code":"55798","system":"gprdproduct"},{"code":"55896","system":"gprdproduct"},{"code":"56","system":"gprdproduct"},{"code":"56013","system":"gprdproduct"},{"code":"56129","system":"gprdproduct"},{"code":"56157","system":"gprdproduct"},{"code":"56279","system":"gprdproduct"},{"code":"56505","system":"gprdproduct"},{"code":"57333","system":"gprdproduct"},{"code":"5735","system":"gprdproduct"},{"code":"57588","system":"gprdproduct"},{"code":"57864","system":"gprdproduct"},{"code":"57882","system":"gprdproduct"},{"code":"57908","system":"gprdproduct"},{"code":"57944","system":"gprdproduct"},{"code":"58258","system":"gprdproduct"},{"code":"58274","system":"gprdproduct"},{"code":"58294","system":"gprdproduct"},{"code":"58451","system":"gprdproduct"},{"code":"58461","system":"gprdproduct"},{"code":"58649","system":"gprdproduct"},{"code":"58682","system":"gprdproduct"},{"code":"59086","system":"gprdproduct"},{"code":"59109","system":"gprdproduct"},{"code":"59271","system":"gprdproduct"},{"code":"59412","system":"gprdproduct"},{"code":"59557","system":"gprdproduct"},{"code":"59603","system":"gprdproduct"},{"code":"59699","system":"gprdproduct"},{"code":"59915","system":"gprdproduct"},{"code":"60067","system":"gprdproduct"},{"code":"60097","system":"gprdproduct"},{"code":"60143","system":"gprdproduct"},{"code":"60232","system":"gprdproduct"},{"code":"60309","system":"gprdproduct"},{"code":"60349","system":"gprdproduct"},{"code":"60465","system":"gprdproduct"},{"code":"6288","system":"gprdproduct"},{"code":"6314","system":"gprdproduct"},{"code":"6362","system":"gprdproduct"},{"code":"6364","system":"gprdproduct"},{"code":"6408","system":"gprdproduct"},{"code":"654","system":"gprdproduct"},{"code":"6765","system":"gprdproduct"},{"code":"6807","system":"gprdproduct"},{"code":"709","system":"gprdproduct"},{"code":"7314","system":"gprdproduct"},{"code":"78","system":"gprdproduct"},{"code":"7806","system":"gprdproduct"},{"code":"80","system":"gprdproduct"},{"code":"8052","system":"gprdproduct"},{"code":"8106","system":"gprdproduct"},{"code":"8800","system":"gprdproduct"},{"code":"9431","system":"gprdproduct"},{"code":"9456","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('acei-loop-diuretic-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acei-loop-diuretic-m1-625mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acei-loop-diuretic-m1-625mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acei-loop-diuretic-m1-625mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
