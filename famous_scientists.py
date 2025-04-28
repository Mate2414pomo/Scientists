# Famous Scientists - Notable scientists and their achievements
import os
import pandas as pd 

scientists = {
    "Albert Einstein": "Developed the theory of relativity.",
    "Isaac Newton": "Formulated the laws of motion and universal gravitation.",
    "Marie Curie": "Pioneered research on radioactivity, first woman to win a Nobel Prize.",
    "Galileo Galilei": "Made fundamental contributions to physics, astronomy, and scientific method.",
    "Charles Darwin": "Developed the theory of evolution by natural selection.",
    "Nikola Tesla": "Invented the AC electricity system and contributed to the development of electromagnetism.",
    "Ada Lovelace": "Known as the first computer programmer.",
    "Stephen Hawking": "Made contributions to cosmology, black holes, and quantum gravity."
}

def list_scientists():
    """Prints a list of famous scientists and their achievements."""
    print("Famous Scientists and Their Achievements:\n")
    for name, achievement in scientists.items():
        print(f"- {name}: {achievement}")

def main():
    list_scientists()

if __name__ == "__main__":
    main()
