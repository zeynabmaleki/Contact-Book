names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Enter a name: ")
    phone_number = input("Enter a phone number: ")

    names.append(name)
    phone_numbers.append(phone_number)


print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print(f"{names[i]}\t\t\t{phone_numbers[i]}")



search_term = input("\nEnter search term: ")
print("Search result:")


if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print(f"Name: {search_term}, Phone Number: {phone_number}")

else:
    print("Name Not Found")