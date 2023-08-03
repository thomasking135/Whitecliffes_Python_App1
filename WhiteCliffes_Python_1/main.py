# Go to the 'View' option and select 'Python Interpreter' from the 'Command Palette'
# In the terminal, enter 'python main.py' to run the console app.

# Main Menu Function
def show_menu():
    print("Cloud X: Black Friday Sale!")
    print("$50 off if you send $200 or more on 5 or more goods")
    print("Menu:")
    print("1) Start")
    "\n"

# Item Choices Function


def show_items():
    print("Available items:")
    print("1) TV $100")
    print("2) Stereo $75")
    print("3) Camera $65")
    print("4) Laptop $90")
    print("5) Ricecooker $50")
    "\n"

# Calculation function


def calculate_total(selected_items):
    prices = [100, 75, 65, 90, 50]
    total = sum(prices[i - 1] for i in selected_items)
    return total

# Display Purchase Function


def display_bought_items(selected_items):
    items_count = {}
    for item in selected_items:
        items_count[item] = items_count.get(item, 0) + 1

    for item, count in items_count.items():
        item_name = {
            1: "TV",
            2: "Stereo",
            3: "Camera",
            4: "Laptop",
            5: "Ricecooker"
        }
        print(f"{count} X {item_name[item]}")

# Main Function


def main():
    while True:
        discount_flag = False  # Reset the discount_flag for each iteration
        total = 0  # Reset the total for each iteration

        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            selected_items = []
            while True:
                show_items()
                item_choice = input(
                    "Select an item number to add (or enter 'n' to finish): ")

                if item_choice == 'n':
                    total = calculate_total(selected_items)
                    if len(selected_items) >= 5 and total >= 200 and not discount_flag:
                        total -= 50
                        discount_flag = True

                    print(f"Total: ${total}")
                    print("-----------")
                    if discount_flag:
                        print(
                            "Congratulations! You have received a $50 discount for purchasing 5 or more items over $200.")

                    if selected_items:
                        print("Items Bought:")
                        display_bought_items(selected_items)
                        print("-----------")

                    break
                elif item_choice.isdigit() and 1 <= int(item_choice) <= 5:
                    selected_items.append(int(item_choice))
                    total = calculate_total(selected_items)
                    print(f"Total: ${total}")
                else:
                    print(
                        "Invalid input. Please enter a valid item number or 'n' to finish.")

        else:
            print("Invalid input. Please select a valid option.")


if __name__ == "__main__":
    main()
