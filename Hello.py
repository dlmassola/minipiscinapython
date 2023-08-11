ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Define the campus information
campus_info = {
    "country": "France",
    "city": "Paris",
    "name": "42"
}

# Define the greetings
greeting_world = "Hello World"
greeting_country = f"{campus_info['country']}!"
greeting_city = f"{campus_info['city']}!"
greeting_name = f"Hello {campus_info['name']}!"

# Modify the data structures
ft_list[1] = "World!"
ft_tuple = ("Hello", greeting_country)
ft_set = {"Hello", greeting_city}
ft_dict["Hello"] = f"{campus_info['name']}{campus_info['city']}!"

# Print the modified data structures
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
