import json
from quantulum import parser # Someone else"s fork because main branch is broken: https://github.com/sohrabtowfighi/quantulum
from tqdm import tqdm
import re

fractionsDict = {"¼": ".25", " 1/4" : ".25",
  "½": ".5", " 1/2:" : ".5",
  "¾": ".75", " 3/4" : ".75",
  "⅐": ".15", " 1/7" : ".15",
  "⅒": ".1", " 1/10" : ".1",
  "⅓": ".33", " 1/3" : ".33",
  "⅔": ".66", " 2/3" : ".66",
  "⅕": ".2", " 1/5" : ".2",
  "⅖": ".4", " 2/5" : ".4",
  "⅗": ".6", " 3/5" : ".6",
  "⅘": ".8", " 4/5" : ".8",
  "⅙": ".17", " 1/6" : ".17",
  "⅚": ".83", " 5/6" : ".83",
  "⅛": ".125", " 1/8" : ".125",
  "⅜": ".375", " 3/8" : ".375",
  "⅝": ".625", " 5/8" : ".625",
  "⅞": ".875" , " 7/8" : ".875", 
  "1/4" : "0.25", "1/2:" : "0.5",
  "3/4" : "0.75", "1/7" : "0.15",
  "1/10" : "0.1", "1/3" : "0.33",
  "2/3" : "0.66", "1/5" : "0.2", 
  "2/5" : "0.4", "3/5" : "0.6", 
  "4/5" : "0.8", "1/6" : "0.17",
  "5/6" : "0.83", "1/8" : "0.125",
  "3/8" : "0.375", "5/8" : "0.625",
  "7/8" : "0.875"}

outJSON = {}
outJSON["recipes"] = []

def hasNumbers(inputString):
	return bool(re.search(r'\d', inputString))

def replaceFractions(ingredientsSplit):
	for i in range(0, len(ingredientsSplit)):
		ingredientsSplit[i] = re.sub(r'\([^)]*\)', '', ingredientsSplit[i]).split(",")[0]
		for fraction in fractionsDict:
			if fraction in ingredientsSplit[i]:
				ingredientsSplit[i] = ingredientsSplit[i].replace(fraction, fractionsDict[fraction])
	return ingredientsSplit

def parseRecipes(recipesJson):
	f = open(recipesJson, "r", encoding="utf-8-sig")
	lines = f.readlines()
	recipes = []
	for line in lines:
		recipe = json.loads(line)
		recipes.append(recipe)
	parsed = []
	for recipe in tqdm(recipes, desc = "Loading recipes"):
		parsed.append({"name" : recipe["name"], "ingredients" : replaceFractions(recipe["ingredients"].split("\n"))})
	return parsed

def main():
	recipesDict = parseRecipes("recipes.json")
	# allIngredients = []
	# for recipe in recipesDict:
	# 	allIngredients.extend(recipe["ingredients"])
	# allIngredients = set(allIngredients)
	# print(allIngredients)

	# Probably need to output this later for iOS use

	#outJSON["recipes"].append({  
						#'name': recipe["name"],
						#'website': 'stackabuse.com',
						#'from': 'Nebraska'})


	#print(allIngredients)
	for recipe in recipesDict:
		recipeIngs = []
		recipeQuants = []
		recipeUnits = []
		for ingredient in recipe["ingredients"]:
			

			# if assd[0].find(",") != -1:
			# 	print(assd[0])
			# 	print(type(assd[0]))
			#print(ingredient)
			try:
				quants = parser.parse(ingredient) # Get rid of extraneous instructions
			except:
				print("WOW: ")
				# We need to manually parse the text
			if len(quants) > 0:
				try:
					if quants[0].unit.name == "dimensionless":
						# We need to manually parse for the object unit (perhaps standardized)
						print(ingredient)
						print(quants)
						pass
					else:
						recipeIngs.append(quants[0].unit.name)
						recipeQuants.append(quants[0].value)
						unitStr = str(quants[0].unit.name)
						recipeUnits.append(str(ingredient[ingredient.find(unitStr) + len(unitStr):]))
					#print(quants[0].__dict__)
					print(quants[0])
					#print(quants[0].unit.name + str(quants[0].value))
				except:
					# We need to manually parse
					pass
		outJSON["recipes"].append({"name": recipe["name"], "ingredients": recipeIngs,"quantities" : recipeQuants, "units" : recipeUnits})

	with open("recipes.txt", "w") as outfile:  
		json.dump(data, outfile)

if  __name__ =="__main__":
	main()