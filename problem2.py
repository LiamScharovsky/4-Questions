
def lastName(authors):
    orderedList = []
  
    for author in authors:
        orderedList.append(author.split())
    authors = []
  
  
    for author in sorted(orderedList, key=lambda author: author[-1].upper()):
        authors.append(' '.join(author))
  

    return authors

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
print(lastName(authors))

# HINT: YOU'LL NEED TO CONVERT EACH PERSON'S NAME (A STRING) INTO A LIST IN ORDER TO GRAB THE LAST NAME BY
# THE INDEX