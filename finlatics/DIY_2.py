#%% Write a program that prompts the user to input a year, checks whether it's a leap year or not, and then prints the result.
def is_leap_year(year):
    return (year % 4 == 0) 

year = int(input("Enter a year: "))
print(f"{year} is {'a' if is_leap_year(year) else 'not a'} leap year.")



# %% Write a Python program that prompts the user to input a word. The program should then determine and output the count of vowels (a, e, i, o, u) in the provided word. Additionally, consider that the word can be in either uppercase or lowercase.
def vowels(word):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    found_vowels = [char for char in word if char.lower() in vowel_list]
    if found_vowels:
        print("The vowels in the word are:", ', '.join(found_vowels))
    else:
        print("There are no vowels in the word.")

user_input = input("Enter your desired word: ")
vowels(user_input)



# %%   Write a Python program that allows the user to input a list of 6 names. After receiving the list, the program should print only the names that start with the letter 'a', regardless of whether the letter is uppercase or lowercase.
def main():
    # Input list of names and print names starting with 'a' (case-insensitive)
    print("\nNames starting with 'a':")
    for i in range(6):
        name = input(f"Enter name {i + 1}: ")
        if name.lower().startswith('a') or name.upper().startswith('A'):
            print(name)

if __name__ == "__main__":
    main()

# %% Write a Python program that takes a list of 10 integers as input. Your program should iterate through the list and print the following:
#         For each even number encountered, print the number squared.
#         For each odd number encountered, print the number cubed.
list = []
for number in range(10):
    number = int(input("The number is:"))
    list.append(number)
print(list)


for number in list:
    if number%2==0:
        print("The number is even and the square of the number would be:",(number**2))
    else:
        print("The number is odd and the cube of the number is:",(number**3))


# %% Imagine you're ordering flowers from a local delivery service. They offer a selection of beautiful flowers, including roses. Each rose is priced at Rs. 10. Along with your choice of roses, you'll need to provide the count of roses you wish to order and the delivery distance. The delivery charges are as follows: Rs. 25 for distances within 5 kilometers, Rs. 50 for distances between 5 and 10 kilometers, and Rs. 75 for distances greater than 10 kilometers. Write a Python program that prompts the user to enter the count of roses and the delivery distance, then calculates and displays the total price to pay, including both the cost of roses and the delivery charge.
roses = int(input("Enter the number of roses needed:"))
distance = float(input("Enter your distance in KM"))

if distance <= 5:
    delivery_charge = 25
    print(f"The delivery charge when {distance} kms is {delivery_charge}")
elif 5 < distance <= 10:
    delivery_charge = 50
    print(f"the delivery charge when {distance} kms is {delivery_charge}")
else:
    delivery_charge = 70
    print(f"The delivery charge when {distance} kms is {delivery_charge}")
price_of_roses = roses*10
       
charge = delivery_charge+price_of_roses
print("The total charge is:",charge)
    
    
    

# %%
