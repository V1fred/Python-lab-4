import requests
import random

API_URL = "https://rickandmortyapi.com/api"

def random_character ():
    response = requests.get (f"{API_URL}/character/{random.randint(1, 826)}")
    return response.json ()  

def search_character (name):
    response = requests.get (f"{API_URL}/character/?name={name}")
    return response.json () ["results"]

def all_locations():
    response = requests.get(f"{API_URL}/location")
    return response.json () ["results"]

def search_episode (id):
    response = requests.get (f"{API_URL}/episode/{id}")   # Небольшое разнообразие)
    return response.json ()



def main ():
    while True:
        
        print ("Well come to Rick and Morty API program")
        print ("Press 1 to get random charecter")
        print ("Press 2 to search character by name")
        print ("Press 3 to get all locations")
        print ("Press 4 to search episode by number (id)")
        print ("Press 5 to exit")

        choice = input ("Your choice: ")

        if choice == "1":
            character = random_character ()
            print (f"Name: {character['name']}, Species: {character['species']}, Status: {character['status']}, Gender: {character['gender']}")

        elif choice == "2":
            name = input ("Input name of character: ")
            characters = search_character (name)
            for character in characters:
                print (f"Name: {character['name']}")

        elif choice == "3":
            locations = all_locations()
            for location in locations:
                print(f"{location['name']}")

        elif choice == "4":
            id = input ("Input number of episode: ")
            episode = search_episode (id)
            print (f"Name: {episode['name']}, Episode: {episode['episode']}")

        elif choice == "5":
            print ("Exit the program")
            print ("Goodbue")
            break
        
        else:
            print ("Invalid input, try again")

main ()