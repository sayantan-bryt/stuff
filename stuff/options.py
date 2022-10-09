import random

ans = ["Aconitum degenii",
        "WhiteGazania",
        "Agapanthus Postbloom",
        "Ageratum houstonianum",
        "Alchemilla alpina",
        "Allium roseum",
        "Alstroemeria aurea",
        "Iceland Plants",
        "Amaranthus tricolor",
        "Amaryllis (Hippeastrum) Flower",
        "Wood anemone",
        "Angelonia salicariifolia",
        "Anthurium1",
        "File-Snapdragons",
        "Aquilegia pyrenaica1JUSA",
        "Purple Milkweed Asclepias purpurascens Ant",
        "Aster amellus sl",
        "Astilbes in the Botanical Garden",
        "Astrantia (Masterwort Plant)",
        "Mauve Flowers",
        "Gypsophila repens",
        "Bachelor's button",
        "Platycodon grandiflorus",
        "Monarda 'Jacob Cline'",
        "Begonia ala de dragÃ",
        "Campanula alpestris",
        "Bergenia cordifolia",
        "Rudbeckia Subtomentosa",
        "Gaillardia",
        "Blazing Star",
        "Bleeding heart",
        "Hyacinthoides",
        "Montane blue-eyed grass",
        "Amsonia ciliata",
        "Starr Bouvardia ternifolia",
        "LS Buddleja 'Buzz Lavender'",
        "Ipomoea leptophylla",
        "Buttercup (Ranunculus)",
        "Calendula officinalis",
        "California poppy",
        "Calla lily",
        "Campanula latifolia1",
        "Iberis (Candytuft)",
        "Canna Lily",
        "Pink Cape Primrose",
        "Ruby-throated hummingbird",
        "Red Carnation Flower",
        "Celosia wool flower",
        "None",
        "Clarkia rubicunda subsp. blasdalei",
        "Clematis x Ivan Olsson",
"Melanargia galathea Drahkrub",
"Cockscomb",
"Aquilegia columbine magpie cultivar",
"Coneflower",
"Heucheraabramsii",
"Coreopsis auriculata",
"Hummel auf Cosmea",
"Cotoneaster-multiflorus",
"Geranium macrorrhizum stempel gespleten",
"CreepingPhlox-CentralMA",
"Crocosmia lucifer",
"Crocus tommasinianus 'Roseus'",
"Fritillaria imperialis 'Crown Imperial'",
"Mannheim Neckarau",
"Cyclamen elegans",
"pseudonarcissus2",
"Dahlia",
"Daisy",
"Daphne bholua",
"Day Lily",
"Delphinium menziesii",
"Adenium obesum (Desert Rose)",
"Blue and gold native bloom",
"Dianthus toletanus Closeup Puertollano",
"Schynige Platte",
"Dietes grandiflora",
"White Dutch irises",
"Wallensteinplatz Echinacea",
"Echium wildpretii",
"English bluebell",
"Erica australis",
"Erigeron glabellus",
"Flower Bed",
"Evening Primrose",
"Yellow - orange flower",
"Euphorbia flower show"
]

options = [["" for j in range(4)] for i in range(len(ans))]

options_file = open('options.txt', 'a')
options_file.write('{')


for i in range(len(ans)):
    num = random.randrange(0,3)
    options[i][num] = ans[i]
    options_file.write('{')
    for j in range(4):
        newnum = random.randrange(len(ans))
        if j != num:
            if newnum == num:
                newnum = (newnum + 1)%(len(ans))
            options[i][j] = ans[newnum]
        options_file.write('"' + str(options[i][j]) + '",')
    options_file.write('},\n')

options_file.write('}')
options_file.close()

print(options)
