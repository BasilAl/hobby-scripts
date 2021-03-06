import os

'''
ς, ε, ρ, τ, υ, θ, ι, ο, π, α, σ, δ, φ, γ, η, ξ, κ λ,
ζ χ ψ ω β ν μ
Ε Ρ Τ Υ Θ Ι Ο Π Α Σ Δ Φ Γ Η Ξ Κ Λ Ζ Χ Ψ Ω Β Ν Μ
Έ Ά Ύ Ί Ό Ή Ώ
έ ά ύ ί ό ή ώ
ϋ ϊ ΐ ΰ
Ϊ Ϋ
'''


char_migrate = {
    "ς": 's',
    'ε': 'e', 'ρ': 'r', "τ": "t", "υ": "y", "θ": "th", "ι": "i", "ο": "o", "π": "p", "α": "a",
    "σ": "s", "δ": "d", "φ": "f", "γ": "g", "η": "i", "ξ": "x", "κ": "k", "λ": "l",
    "ζ": "z", "χ": "x", "ψ": "ps", "ω": "o", "β": "v", "ν": "n", "μ": "m",
    "Ε": "e", "Ρ": "r", "Τ": "t", "Υ": "y", "Θ": "th", "Ι": "i", "Ο": "o", "Π": "p", "Α": "a",
    "Σ": "s", "Δ": "d", "Φ": "f", "Γ": "g", "Η": "i", "Ξ": "x", "Κ": "k",
    "Λ": "l", "Ζ": "z", "Χ": "x", "Ψ": "ps", "Ω": "o", "Β": "v", "Ν": "n", "Μ": "m",
    "Έ": "e", "Ά": "a", "Ύ": "y", "Ί": "i", "Ό": "o", "Ή": "i", "Ώ": "o",
    "έ": "e", "ά": "a", "ύ": "y", "ί": "i", "ό": "ο", "ή": "i", "ώ": "o",
    "ϋ": "i", "ϊ": "i", "ΐ": "i", "ΰ": "i",
    "Ϊ": "i", "Ϋ": "i"
}


#Example in folder
os.chdir('C:/Users/alift/Desktop/RenameTestFolder')
for f in os.listdir():
    name = f
    new_name = ""
    # print(f)
    for l in name:
        if l in char_migrate:
            b = char_migrate[l]
            new_name += b
        else:
            new_name += l

    os.rename(f, new_name)
