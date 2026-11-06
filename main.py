from pyscript import document
# Dictionary containing planet information

non-metals= {{"H": ("Hydrogen", 1, 1.008), "He": ("Helium", 2, 4.002), "F": ("Flourine", 9, 19.00), "Ne": ("Neon", 10, 20.18), "P": ("Phosphorus", 15, 30.97), "C": ("Carbon", 6, 12.01), "N": ("Nitrogen", 7, 14.007), "O": ("Oxygen", 8, 15.999), "S": ("Sulfur", 16, 32.06), "Cl": ("Chlorine", 17, 35.45), "Se": ("Selenium", 34, 78.96), "Br": ("Bromine", 35, 79.90), "I": ("Iodine", 53, 126.90), "Ar": ("Argon", 18, 39.95), "Kr": ("Krypton", 36, 83.80), "Xe": ("Xenon", 54, 131.29), "Rn": ("Radon", 86, 222),}}
# planets= {"MERCURY":("Mercury", 1, 0), "VENUS" :("Venus", 2, 0)}
# #Planet name, Order from the Sun, # of moons
# #KEY : VALUE

# Function to search for a planet
def search_element(e):
    # Get the input FROM HTML
    Planet1 = document.getElementById("planet1").value
    # Retrieve information from dictionary
    result = planets.get(Planet1, ("Planet not found", "-", "-"))
    # Display the result in HTML
    # Planet Code, Name, Order, Moons
    document.getElementById("code").innerText = Planet1
    document.getElementById("name").innerText = result[0]
    document.getElementById("order").innerText = result[1]
    document.getElementById("moons").innerText = result[2]

