import sys
import argparse
import os
import requests
import json

data_default = {
    "ID" : 0,
    "Description" : "",
    "Amount" : 0
}


list_default = [
    {
        "ID" : 0,
        "Description" : "",
        "Amount" : 0
    }
]

file_name = "tracky.json"


# Read is there any data and Create there isnt any data (file)
def ReadFile():
    try :
        with open (file_name, 'r') as json_file:
            datalama = json.load(json_file)
            return datalama
    except :
        with open (file_name, 'w') as json_file:
            json.dump(data_default, json_file, indent=4)


def WriteFile(result):
    with open (file_name, 'w') as json_file:
        json.dump(result, json_file, indent=4)


            
# Add object and amount into list with some ID
def Add(idlama, object, amount):
    data_default["ID"] = idlama + 1
    data_default["Amount"] = amount
    data_default["Description"] = object
    data_updated = data_default
    return data_updated



def main():
    if len(sys.argv) < 2 :
        print("Tracker.py Usage : Tracking Application for Money Expanses !")
        print("Ex : python tracker.py <choices_for_notes> ")
        print("Choices : <add> , <list>, <delete>, <total>")
    parser = argparse.ArgumentParser(description="Usage  : Tracking Application for Money Expanses")
    parser.add_argument("notes", choices=["add", "list", "delete", "total"], help="The operation to perform.")
    parser.add_argument("--description", "-d",type=str, help= "Object description")
    parser.add_argument("--amount","-a", type=float, help="Amount for object" )

    args = parser.parse_args()

    if args.notes == "add":
        print(f"Inserting {args.description} with Rp.{args.amount} into tracking notes !")
        desc = args.description
        amount = args.amount
        datalama = ReadFile()
        try : 
            idlama = datalama[-1]["ID"]
            result = Add(idlama, desc, amount)
            datalama.append(result)
            WriteFile(datalama)
        except :
            WriteFile(list_default)



    elif args.notes == "list" :
        print("list")
    elif args.notes == "delete":
        print("delete")
    elif args.note == "total" :
        print("total")


if __name__ == '__main__' :
    main()

