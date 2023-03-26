from csv import reader, DictReader
from sys import argv, exit


def main():
   
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    arquivos_csv = argv[1]
    arquivos_txt = argv[2]
   
    with open(arquivos_csv, "r") as arquivo_csv:
        ler_csv = DictReader(arquivo_csv)
        dict = list(ler_csv)
    
    with open(arquivos_txt, "r") as file:
        ler_sequencia = file.read()
   
    sequencia_max_STR = []

    for i in range(1, len(ler_csv.fieldnames)):
        STR = ler_csv.fieldnames[i]
        sequencia_max_STR.append(0)
     
        for j in range(len(ler_sequencia)):
            STR_count = 0
            
            if ler_sequencia[j:(j + len(STR))] == STR:
                k = 0
                while ler_sequencia[(j + k):(j + k + len(STR))] == STR:
                    STR_count += 1
                    k += len(STR)
                
                if STR_count > sequencia_max_STR[i - 1]:
                    sequencia_max_STR[i - 1] = STR_count
    
    for i in range(len(dict)):
        matches = 0
        for j in range(1, len(ler_csv.fieldnames)):
            if int(sequencia_max_STR[j - 1]) == int(dict[i][ler_csv.fieldnames[j]]):
                matches += 1
            if matches == (len(ler_csv.fieldnames) - 1):
                print(dict[i]['name'])
                exit(0)
    print("No match")


main()