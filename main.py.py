from functions import get_valid_name, get_valid_number

def building_datasets() -> list:
    """Builds and returns a list of structured datasets."""
    dictionaries = [] 
    numbers_dictionaries = get_valid_number("How many datasets? (positive integer):", minimum_value=1)
    
    for i in range(1, numbers_dictionaries + 1):
        name_set = get_valid_name(f"Enter the name of the {i}° dataset: ")
        
        storage_elements = []
        number_elements = get_valid_number("How many elements? (>0):", minimum_value=1)
        
        for element in range(1, number_elements + 1):
            print(f"\nEntering data for element {element}: ")
            element_data = {}
            
            couples = get_valid_number("How many key-value pairs do you want to insert?", minimum_value=1)
            
            for _ in range(couples):
                key = input("Enter a key: ").title()
                key_value = input("Enter the value for the key: ").title()
                element_data[key] = key_value

            storage_elements.append(element_data)
    
        dictionaries.append({"Name": name_set, "Data": storage_elements})
        print("\n")

    return dictionaries

def add_elements(dataset):
    number_new_elements=get_valid_number("\nHow many elements do you want add?", minimum_value=1)
    for i in range(number_new_elements):
        storage_elements={}
        couples=get_valid_number("How many data's couples do you want enter (integer positive number):", minimum_value=1)
        for j in range(couples):
            key=get_valid_name("Enter a key: ")
            key_value=get_valid_name("Enter a value of your key: ")
            storage_elements[key]=key_value   
        
    dataset["Data"].append(storage_elements)
    # print(f"New {dataset['Name']}:\n{dataset['Data']}")
    print(f"\n{dataset['Name']} Updated:\n")
    for idx, element in enumerate(dataset["Data"], start=1):
        print(f"{idx}. {element}")
    print("\n")

def remove_elements(dataset):
    number_removed_elements=get_valid_number("\nHow many elements do you want remove?",minimum_value=1)
    for i in range(number_removed_elements):
        while True:
            index=get_valid_number("Which element do you want remove? ")
            
            if index>0 and index<=len(dataset["Data"]):
                deleted_element=dataset["Data"].pop(index-1)
                print(f"Removed: {deleted_element}")
                break #I'm getting out of the cycle

            elif index<=0 or index>len(dataset["Data"]):
                print(f"Error: Enter a number among [1,{len(dataset["Data"])}].",end=" ")

    print(f"\n{dataset['Name']} Updated:\n")
    for idx, element in enumerate(dataset["Data"], start=1):
        print(f"{idx}. {element}")
    print("\n")

def main():
    """Main function that manages the interactive menu."""
    print("Hello, I can create Data-Sets.")
    management = building_datasets()

    while True:
        first_choice=input("Do you want change something in your Data-Sets? Press yes/no: ").lower()
        if first_choice=="yes":
            while True:
                index = get_valid_number("\nWhich Data-Set do you want change? ", minimum_value=1)
                
                if index <= len(management):
                    break
                print(f"Error: Enter a number between 1 and {len(management)}.")
                
            print("\nMenù:")
            print("1.Add elements\n2.Remove elements")
            choiches=["add","remove","replace"]
            second_choice=input(f"Make your choice among {choiches}: ").strip().lower()

            if second_choice==choiches[0]: # Add elements
                print(f"\nYou want add elements in: {management[index-1]['Name']}")
                add_elements(management[index-1])

            elif second_choice==choiches[1]: # Remove elements
                print(f"\nYou want remove elements in {management[index-1]['Name']}")
                remove_elements(management[index-1])
        
        elif first_choice=="no": #Breaking the script
            print("\nThanks for your time, see you soon.")
            break        


# ENTRY POINT STANDARD SENIOR
if __name__ == "__main__":
    main()