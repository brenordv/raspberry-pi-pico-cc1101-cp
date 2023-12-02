import random

# List of funny English words
funny_words = [
    "Kumquat", "Zucchini", "Artichoke", "Brussels Sprout",
    "Cantaloupe", "Dragonfruit", "Elderberry", "Fennel",
    "Guava", "Huckleberry", "Jicama", "Kohlrabi",
    "Lychee", "Mango", "Nectarine", "Okra",
    "Papaya", "Quince", "Rutabaga", "Shallot",
    "Tamarind", "Ugli Fruit", "Watermelon", "Yam",
    "Armadillo", "Bison", "Chinchilla", "Dugong",
    "Echidna", "Flamingo", "Gazelle", "Hippopotamus",
    "Iguana", "Jellyfish", "Kangaroo", "Lemur",
    "Meerkat", "Narwhal", "Ocelot", "Pangolin",
    "Quokka", "Raccoon", "Salamander", "Tapir",
    "Uakari", "Vulture", "Walrus", "Xerus",
    "Yak", "Zebu",
    "Acacia", "Begonia", "Crocus", "Daffodil",
    "Eucalyptus", "Freesia", "Gardenia", "Hyacinth",
    "Iris", "Jasmine", "Kale", "Lavender",
    "Marigold", "Nasturtium", "Orchid", "Petunia",
    "Quince", "Rose", "Sunflower", "Tulip",
    "Umbrella Plant", "Violet", "Willow", "Xerophyte",
    "Yucca", "Zinnia"
]


def get_random_word():
    return random.choice(funny_words)
