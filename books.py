
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--filter', type=str,
                    help="show a subset of books, looks for the argument as a substring of any of the              fields")
parser.add_argument("--year", action="store_true", help="sort the books by year, ascending instead of default sort")
parser.add_argument("--reverse", action="store_true", help="reverse sort")
try:
    args = parser.parse_args()
except SystemExit:
    print("Undefined arguments!")


def find(items, term, key):
    return [item[key] for item in items if item["id"] == term]

def createList(dic):

    #Extract file types
    types = []
    for elm in dic:
        types.append(elm['id'])

    # Initiaite the output list
    aList = []
    # Explore the directory
    for filename in os.listdir(os.getcwd()):
        # Find specific input file types
        if filename in types:
            file = open(filename, "r")
            lines = file.readlines()
            file.close()
            # Find the seperator based on type
            seperator = find(dic, filename, "sep")[0]
            # Find the order of items in a row based on type
            seq = find(dic, filename, "seq")[0]
            for line in lines:
                item = line.strip().split(seperator)
                # Recorder the items in each row
                item_adj = [item[seq[0]].strip(), item[seq[1]].strip(), item[seq[2]].strip(), item[seq[3]].strip()]
                aList.append(item_adj)

    # Convert the year from string to integer
    for item in aList:
        item[3] = int(item[3])

    # Default output
    return aList

def changeList(out, args):

    if args.filter:
        filterArray =[]
        for elm in out:
            line =  "%s %s %s %s" %(elm[0],elm[1],elm[2],str(elm[3]))
            if args.filter.lower() in line.lower():
                filterArray.append(elm)
        out = filterArray

    if args.year:
        sortColumn = 3
    else:
        sortColumn = 0

    if args.reverse:
        out = sorted(out, key=lambda x: x[sortColumn], reverse =True)
    else:
        out = sorted(out, key=lambda x: x[sortColumn])

    return out

def main():

    #Dictionary of input files
    dic = [{"id" :"csv", "sep": ",", "seq": [1, 2, 0, 3]},
           {"id": "pipe", "sep": "|", "seq" : [1, 0, 2, 3]},
           {"id": "slash", "sep": "/", "seq": [2, 1, 3, 0]}
           ]


    #Call createList function to extract data from input files
    out = createList(dic)

    #Call changeList function to consider input arguments
    out = changeList(out, args)

    #Print the final output
    for elm in out:
        print("%s, %s, %s, %s" %(elm[0],elm[1],elm[2],str(elm[3])))

if __name__ == "__main__":
    main()
