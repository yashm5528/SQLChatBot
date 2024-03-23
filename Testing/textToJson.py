import json
import os

def convert(file):
    finalDict = {}

    with open(file) as fh:
        l = 1
        for line in fh:
            splitData2 = list(line.strip().split(" ||| ", 2))
            print(splitData2)
            uid = 'query' + str(l)
            i = 0
            dict = {}
            fields = ["HumanQuery", "SQLQuery"]

            while i < len(fields):
                dict[fields[i]] = splitData2[i]
                i = i + 1

            finalDict[uid] = dict
            l = l + 1
    fileName = os.path.basename(file)
    outFile = os.path.join(r"C:\Users\anark\Desktop\Capstone\Implementation\Modulated_code\Testing", f"{fileName}.json")
    out_file = open(outFile, "w")
    json.dump(finalDict, out_file, indent=4)
    out_file.close()

convert('Testing\geography.uw.test.txt')
convert('Testing\geography.uw.train.txt')
convert('Testing\geography.uw.dev.txt')