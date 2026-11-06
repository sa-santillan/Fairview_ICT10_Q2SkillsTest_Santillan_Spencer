# Skills Test
from pyscript import document, when

nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.002),
    "F": ("Fluorine", 9, 19.00),
    "Ne": ("Neon", 10, 20.18),
    "P": ("Phosphorus", 15, 30.97),
    "C": ("Carbon", 6, 12.01),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Se": ("Selenium", 34, 78.96),
    "Br": ("Bromine", 35, 79.90),
    "I": ("Iodine", 53, 126.90),
    "Ar": ("Argon", 18, 39.95),
    "Kr": ("Krypton", 36, 83.80),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222)
}

def search_element(event):

    Nonmetal1 = document.getElementById("nonmetal1").value.strip()

    result = nonmetals.get(Nonmetal1, ("Non-metal not found", "-", "-"))

    document.getElementById("symbol").innerText = Nonmetal1
    document.getElementById("name").innerText = result[0]
    document.getElementById("atomic_number").innerText = result[1]
    document.getElementById("atomic_mass").innerText = result[2]
