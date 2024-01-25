import pickle
import os


def main():
    while True:
        print("What would you like to do?")
        print("1. Create a new list")
        print("2. View / edit an existing list")
        print("3. Exit the program")

        choice = input("Select (1 - 3): ")

        if choice == "1":
            create_list()
        elif choice == "2":
            choose_list()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose between options 1 - 3.")


def create_list():
    while True:
        list_name = (input("Name your list: ")).strip().upper()
        if not list_name:
            print("The Name of your list must contain characters.")
            continue

        existing_lists = get_existing_lists()

        if list_name in existing_lists:
            print(f"A list named {list_name} already exists. Please choose a different name.")
        else:
            break

    my_list = []

    while True:
        item = input(f"Enter an item to add to {list_name} (or press 'Enter' to finish): ")

        if not item:
            break

        my_list.append(item)

        print(f"{list_name}:")
        for i, element in enumerate(my_list, start=1):
            print(f"{i}. {element}")

    save_list(list_name, my_list)


def save_list(list_name, my_list):
    try:
        with open(f"{list_name}.pkl", "wb") as file:
            pickle.dump(my_list, file)
            print("List saved!")
    except Exception:
        print("Error saving list.")


def choose_list():
    existing_lists = get_existing_lists()

    if not existing_lists:
        print("There are no existing lists.")
        return

    print("Existing lists:")
    for i, list_name in enumerate(existing_lists, start=1):
        print(f"{i}. {list_name}")

    while True:
        selected_index = input(
            "Select the number of the list you want to access (or press 'ENTER' to return to main menu): ")

        if selected_index == "":
            break

        try:
            selected_index = int(selected_index)
            if 1 <= selected_index <= len(existing_lists):
                selected_list_name = existing_lists[selected_index - 1]
                edit_list(selected_list_name)
                break
            else:
                print("Invalid input. Please select a valid list number.")
        except ValueError:
            print("Invalid input. Please enter a valid list number.")


def edit_list(list_name):
    with open(f"{list_name}.pkl", "rb") as file:
        my_list = pickle.load(file)

    print(f"{list_name}")
    for i, item in enumerate(my_list, start=1):
        print(f"{i}. {item}")

    while True:
        print(f"____OPTIONS_for_list_{list_name}____")
        print("1. Add new items")
        print("2. Remove items")
        print(f"3. Save changes and exit the list")
        print("4. Delete the list")

        option = input("Select an option (1 - 4): ")

        if option == "1":
            while True:
                print(f"{list_name}")
                for i, item in enumerate(my_list, start=1):
                    print(f"{i}. {item}")
                new_item = input(
                    f'Enter a new item to be added to {list_name} (or press "Enter" to go back to OPTIONS for {list_name}): ')
                if not new_item:
                    break
                my_list.append(new_item)
                print(f"Item added.")


        elif option == "2":
            while True:
                print(f"{list_name}")
                for i, item in enumerate(my_list, start=1):
                    print(f"{i}. {item}")
                index_to_remove = input(
                    f"Enter the number of the item to be removed (or press 'Enter' to go back to OPTIONS for {list_name}): ")

                if not index_to_remove:
                    break

                try:
                    index_to_remove = int(index_to_remove)

                    if 1 <= index_to_remove <= len(my_list):
                        del my_list[index_to_remove - 1]
                        print(f"Item removed.")

                    else:
                        print("Invalid input.")

                except ValueError:
                    print("Invalid input. ")


        elif option == "3":
            with open(f"{list_name}.pkl", "wb") as file:
                pickle.dump(my_list, file)
                print("List updated and saved.")
            break  # Exit the loop and return to the main menu

        elif option == "4":
            confirm_delete = input(
                f"Are you sure you want to delete the list {list_name}? Enter 'y' to confirm: ").lower()
            if confirm_delete == "y":
                os.remove(f"{list_name}.pkl")
                print(f"List {list_name} deleted.")
                break
            else:
                print(f"Did not delete list {list_name}.")

        else:
            print("Invalid input. Please choose between options 1 - 4.")


def get_existing_lists():
    # Get a list of existing lists (files with _list.pkl extension)
    files = [f for f in os.listdir() if f.endswith(".pkl")]
    return [f.replace(".pkl", "") for f in files]


if __name__ == "__main__":
    main()
