import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

outJSON = {}
outJSON["ingredients"] = []

class Result:
    def __init__(self, id, quantity, image):
        self.id = id
        self.quantity = quantity
        self.image = image

    def __str__(self):
        string = "| Product: " + self.id + " | Quantity: " + self.quantity.text + " | ImageLink: " + self.image["src"]
        return string


def get_results(query):
    link = "https://shop.thefreshgrocer.com/store/e7e1123699/search?query=" + query
    response = requests.get(link)
    text = response.text

    if "noSearchResults" in text:
        return []
    else:
        soup = BeautifulSoup(text)

        # Get products
        products = soup.find_all("div", attrs={"class": ["product", "productBox"]})

        if products:
            results = []

            for product in products:
                id = product["id"]
                quant = product.find("span", attrs={"class": "sizeInfo__currentValue"})
                img = product.find("img", attrs={"class": "product__image"})
                result = Result(id, quant, img)

                results.append(result)

            # Get quantities
            # quantities = soup.find_all("span", attrs={"class": "sizeInfo__currentValue"})
            quantities = []
            for res in results:
                quantities.append(res.quantity)

            values = [tag.text for tag in quantities]

            # Get images
            #images = soup.find_all("img", attrs={"class": "product__image"})

            # Build a frequency dictionary and sort it
            freq_dict = {}

            for val in values:
                if val not in freq_dict:
                    freq_dict[val] = 1
                else:
                    freq_dict[val] += 1

            freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1]))
            #print(freq_dict)
            reverse_quants = list(freq_dict.values())[::-1]
            freq_quants = reverse_quants[:3]

            # Get the three most frequented items based on the frequency
            #print(freq_quants)
            freq_results = []
            checked = []

            for res in results:
                le_quant = res.quantity.text
                if freq_dict[le_quant] in freq_quants and le_quant not in checked:
                    freq_results.append(res)
                    checked.append(le_quant)

            return freq_results


if __name__ == "__main__":
    #le_query = "ommit commit"
    #freqs = get_results(le_query)

    file = open("allingredients_1.txt")
    ingredient_list = file.read().split()

    for le_query in tqdm(ingredient_list, "Searching for ingredients..."):
        freqs = get_results(le_query)
        if freqs:
            for item in freqs:
                #print(item)
                outJSON["ingredients"].append({"query": le_query, "quantity": item.quantity, "image": item.image})

    with open("frequent_ingredients.json", "w") as outfile:
        json.dump(outJSON, outfile)