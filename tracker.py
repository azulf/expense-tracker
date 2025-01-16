import sys
import argparse
import os
import requests
import json
from datetime import datetime

data_default = {
    "ID" : 0,
    "Description" : "",
    "Amount" : 0,
    "Date"  : "",
    "Month" : ""
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
    now = datetime.now()
    data_default["ID"] = idlama + 1
    data_default["Amount"] = amount
    data_default["Description"] = object
    data_default["Date"] = now.strftime(("%m-%d-%Y, %H:%M:%S"))
    data_default["Month"] = now.strftime("%B")
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
    parser.add_argument('-x', type=int, help = "Delete this ID" )
    parser.add_argument('--month','-m', type=str, help = "Insert Month for List")
    
    args = parser.parse_args()


    # Add Function
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


    # List Function
    elif args.notes == "list" :
        print("ID \t Description \t Amount \t\t Month" )
        list_all_data = ReadFile()
        if args.month :
            list_all_data = [item for item in list_all_data if item ['Month'] == args.month]
            for item in list_all_data:
                print(f"{item['ID']} \t {item['Description']} \t\t {item['Amount']} \t\t {item['Month']}")
        else :
            try :
                for item in list_all_data:    
                    print(f"{item['ID']} \t {item['Description']} \t\t {item['Amount']} \t\t {item['Month']}")
            except : 
                print("Data not found")
        
    # Delete 1 of Listed Data
    elif args.notes == "delete":
        data_delete = ReadFile()
        x = args.x
        print(f"Deleting List with ID : {args.x}")
        data_delete = [item for item in data_delete if item["ID"] != x] 
        WriteFile(data_delete)

    # Total Amount of Listed Data
    elif args.notes == "total" :
        print("total Amount of expenses")
        total_amount_data = ReadFile()
        total_amount = 0
        try : 
            for item in total_amount_data:
                total_amount += item['Amount']
        except :
            print(f"Total still 0")
        print(f"Total amount expanses for all month : {total_amount}")

if __name__ == '__main__' :
    main()

