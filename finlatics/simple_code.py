#%%
name=input("Enter you name:")
print("Hello " +name+ "! let's plan an exciting weekend activity.")
print("You have a free weekend ahead.How would you like to plan it?")
print("1: Go for a hike in the mountains")
print("2: attend a music concert in the city")
print("3: Go for a beach")

choice=input("enter you preferred activity among (1,2,3):")
if choice == "1":
    print("what difficulty level do u prefer?")
    print("a:easy")
    print("b:moderate")
    print("c:difficult")

    difficulty_level=input("Choose your difficulty level (a,b,c)")
    if difficulty_level == "a":
        print("You enjoyed a scenic view")
    elif difficulty_level == "b":
        print("It was a moderate level hike where you overcame some challenges")
    elif difficulty_level == "c":
        print("a difficult hike where you overcame all the challenges")
    else:
        print("choice not made for difficulty") 


elif choice == "2":
    genre=input("Your fav genre among (jazz,pop,classical)")
    # print(f"You had fun and enjoyed your fav {genre} music in your fav city")
    if genre == "jazz":
        print(f"You had fun and enjoyed your fav {genre} music in your fav city")
    elif genre == 'pop':
        print(f"You had fun and enjoyed your fav {genre} music in your fav city")
    elif genre == 'classical':
        print(f"You had fun and enjoyed your fav {genre} music in your fav city")
    else:
        print("choice not available")
 
            
elif choice == "3":
    print("You got to spend a relaxing day at the beach among the waves")


else:
    print("Not valid choice. choose one among 1,2,3")
    
print("thank you for planning your weekend with us"+name+"!")

    
# %%
