import json
from quantulum import parser  # Someone else"s fork because main branch is broken: https://github.com/sohrabtowfighi/quantulum
from quantulum import load as l
from tqdm import tqdm
import re
import sys
import nltk

fractionsDict = {"¼": ".25", " 1/4": ".25",
				 "½": ".5", " 1/2:": ".5",
				 "¾": ".75", " 3/4": ".75",
				 "⅐": ".15", " 1/7": ".15",
				 "⅒": ".1", " 1/10": ".1",
				 "⅓": ".33", " 1/3": ".33",
				 "⅔": ".66", " 2/3": ".66",
				 "⅕": ".2", " 1/5": ".2",
				 "⅖": ".4", " 2/5": ".4",
				 "⅗": ".6", " 3/5": ".6",
				 "⅘": ".8", " 4/5": ".8",
				 "⅙": ".17", " 1/6": ".17",
				 "⅚": ".83", " 5/6": ".83",
				 "⅛": ".125", " 1/8": ".125",
				 "⅜": ".375", " 3/8": ".375",
				 "⅝": ".625", " 5/8": ".625",
				 "⅞": ".875", " 7/8": ".875",
				 "1/4": "0.25", "1/2:": "0.5",
				 "3/4": "0.75", "1/7": "0.15",
				 "1/10": "0.1", "1/3": "0.33",
				 "2/3": "0.66", "1/5": "0.2",
				 "2/5": "0.4", "3/5": "0.6",
				 "4/5": "0.8", "1/6": "0.17",
				 "5/6": "0.83", "1/8": "0.125",
				 "3/8": "0.375", "5/8": "0.625",
				 "7/8": "0.875", "-1/4": "0.25", "-1/2:": "0.5",
				 "-3/4": "0.75", "-1/7": "0.15",
				 "-1/10": "0.1", "-1/3": "0.33",
				 "-2/3": "0.66", "-1/5": "0.2",
				 "-2/5": "0.4", "-3/5": "0.6",
				 "-4/5": "0.8", "-1/6": "0.17",
				 "-5/6": "0.83", "-1/8": "0.125",
				 "-3/8": "0.375", "-5/8": "0.625",
				 "-7/8": "0.875"}

outJSON = {}
outJSON["recipes"] = []


def hasNumbers(inputString):
	return bool(re.search(r'\d', inputString))


def cleanStr(ingredientsSplit):
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
	for recipe in tqdm(recipes, desc="Loading recipes"):
		#tempYield = 2
		if "recipeYield" in recipe and "image" in recipe:
			#tempYield = recipe["recipeYield"]
			parsed.append({"name": recipe["name"], "yield" : recipe["recipeYield"], "image" : recipe["image"], "ingredients": cleanStr(recipe["ingredients"].split("\n"))})
	return parsed


def deleteUnits(ingredient, units):
	"""ingredient = 300ml/10fl oz double cream --> Original ingredient full string
		units = [ml, fl oz] --> List of detected units by quantulum"""

	#print("Ingredient -> ", ingredient, "| Units ->", units)

	# For all the units detected in the ingredient
	for unit in units:

		correct_unit = None
		# Check if the unit is the correct key for the json database
		try:
			correct_unit = l.NAMES[unit]
		except KeyError:
			temp_units = unit.split()
			for temp_unit in temp_units:
				if temp_unit in list(l.NAMES.keys()):
					correct_unit = l.NAMES[temp_unit]
					break
			if not correct_unit:
				correct_unit = l.NAMES["cup"]

		# If the unit has symbols (ml, fl oz, etc)
		if correct_unit.symbols:
			# Search for all the occurences of the symbols in the string and substring everything after the occurences
			symbols = correct_unit.symbols
			for symb in symbols:
				if symb in ingredient:
					ingredient = str(ingredient[ingredient.find(symb) + len(symb):])
					# Remove unnecessary periods
					#ingredient = ingredient.replace(".", "")

		# If the unit doesn't have symbols (cup, drop, bar) OR if the unit is LITERALLY written in the string ("tablespoons", "meters")...
		pluralUnit = unit + "s"

		# Check if either the singular (cup) or plural (cups) versions of the unit are in the string
		if pluralUnit in ingredient:
			ingredient = str(ingredient[ingredient.find(pluralUnit) + len(pluralUnit):])
		elif unit in ingredient:
			ingredient = str(ingredient[ingredient.find(unit) + len(unit):])

		# Make sure that we have covered the pound-mass case
		if unit == "pound-mass":
			if "pound" in ingredient:
				ingredient = str(ingredient[ingredient.find("pound") + len("pound"):])

	# Remove leading whitespace
	try:
		if ingredient[0] == " ":
			ingredient = ingredient.lstrip(" ")
	except:
		pass

	return ingredient

def stemIngredient(ingredient):

	regex = re.compile('[^a-zA-Z]')
	ingredient = regex.sub('', ingredient)

	ingredientTokenized = nltk.pos_tag(nltk.tokenize.word_tokenize(ingredient))
	newIngredient = "" 
	for pair in ingredientTokenized:
		if pair[1] != 'VB' and pair[1] != 'JJ':
			newIngredient += pair[1] + " "
	newIngredient.rstrip()
	newIngredient = newIngredient.split(" ")
	newIngredientLen = len(newIngredient)
	if newIngredientLen == 1:
		newIngredient = newIngredient[0]
	else:
		newIngredient = newIngredient[newIngredientLen-2] + " " + newIngredient[newIngredientLen-1]
	return newIngredient

def main():
	completeListIngredients = []
	recipesDict = parseRecipes("recipes.json")
	# allIngredients = []
	# for recipe in recipesDict:
	#   allIngredients.extend(recipe["ingredients"])
	# allIngredients = set(allIngredients)
	# print(allIngredients)

	# Probably need to output this later for iOS use

	# outJSON["recipes"].append({
	# 'name': recipe["name"],
	# 'website': 'stackabuse.com',
	# 'from': 'Nebraska'})

	# print(allIngredients)
	for recipe in tqdm(recipesDict, desc="Generating JSON files"):
		recipeNumsList = []
		recipeUnitsList = []
		recipeContent = []

		for ingredient in recipe["ingredients"]:
			#print("FIRST PARSE", ingredient)

			is_dimensionless = False

			# Do some string cleanup
			ingredient = ingredient.lower()
			# Replace weird 1-1/2 notation
			ingredient = re.sub("(\d)\-(\d/\d)", r"\1 \2", ingredient)

			# if assd[0].find(",") != -1:
			#   print(assd[0])
			#   print(type(assd[0]))
			try:
				quants = parser.parse(ingredient)  # Get rid of extraneous instructions

			except:
				# Tackling the case where there are quantities but not units
				if any(char.isdigit() for char in ingredient):
					res = re.findall(r'\d+', ingredient)
					quantity = res[0]
					parsedIngredient = ingredient[ingredient.find(str(quantity)) + len(str(quantity)):]
					parsedIngredient = stemIngredient(parsedIngredient)
					if not re.match("^[0-9 ]+$", parsedIngredient):
						recipeNumsList.append(quantity)
						recipeContent.append(parsedIngredient)
					continue

			if quants:
				if len(quants) > 0:

					#print("Length of quants is:", str(len(quants)))
					# Lists to add to recipeNumsList and recipeUnitsList in case we have more than 2 nums/units
					recipeNums = []
					recipeUnits = []

					for quant in quants:
						#print("NAME " + quant.unit.name)

						# If there aren't any units identified
						if quant.unit.name == "dimensionless":
							is_dimensionless = True
							#print("Got to dimensionless!!")
							# Either there is a number and the ingredient is "3 pieces of meat"
							if any(char.isdigit() for char in ingredient):
								numStr = str(quant.value)
								#print("numStr " + numStr)
								ingredient = ingredient[ingredient.find(numStr) + len(numStr):].lstrip(" ")
								ingredient = stemIngredient(ingredient)
								if not re.match("^[0-9 ]+$", ingredient):
									if quant.value not in recipeNums:
										recipeNums.append(quant.value)
									if ingredient not in recipeContent:
										recipeContent.append(ingredient)
									recipeUnits.append("")
							# Or there isn't any number and we just append the ingredient
							else:
								ingredient = stemIngredient(ingredient)
								if not re.match("^[0-9 ]+$", ingredient):
									if ingredient not in recipeContent:
										recipeContent.append(ingredient)
									recipeUnits.append("")
						else:
							if not re.match("^[0-9 ]+$", str(quant.unit.name)):
								if quant.value not in recipeNums:
									recipeNums.append(quant.value)
								recipeUnits.append(str(quant.unit.name))

						# except Exception as e:
						#     #print(trap)
						#     raise e
						#     pass

					if not is_dimensionless:
						cleanIngredient = deleteUnits(ingredient, recipeUnits)
						cleanIngredient = stemIngredient(cleanIngredient)
						if not re.match("^[0-9 ]+$", cleanIngredient):
							recipeContent.append(cleanIngredient)
					recipeUnitsList.append(recipeUnits)
					recipeNumsList.append(recipeNums)
				else:
					#print("SHOULD WE EVEN BE HERE EMPTY ER: " + ingredient)
					recipeContent.append(ingredient)

		#print(recipe["name"])
		#print(recipeNumsList)
		#print(recipeUnitsList)
		#print(recipeContent)
		completeListIngredients.extend(recipeContent)
		#print("______________________")
		outJSON["recipes"].append(
			{"name": recipe["name"], "yield": recipe["yield"], "image": recipe["image"], "quantities": recipeNumsList, "units": recipeUnitsList, "content": recipeContent})

	with open("recipesjson.txt", "w") as outfile:
		json.dump(outJSON, outfile)

	with open("allingredients.txt", "w") as final_file:
		final_file.write(str(set(completeListIngredients)))
		final_file.close()


if __name__ == "__main__":
	main()


# sample_ingredients = ["0.75 cups M&Ms", 3 Tablespoons Grainy Dijon Mustard", "1 tbsp demerara sugar", "1 – 14 oz. can of creamed corn", "0.33 cup brown sugar", "100g/4oz parmesan", "1 1/2 cups canned pumpkin", "1 teaspoons vanilla extract"]
# clean_ingredients = []

# for ingredient in sample_ingredients:
#   # Initialize a list of units
#   unitList = []
#   try:
#       quants = parser.parse(ingredient) # Get rid of extraneous instructions
#   except:
#       pass
#       #print("Hmmm")
#       print(ingredient, "COULDNT BE PARSED LELZ")

#   if len(quants) > 0:
#       try:
#           for quant in quants:
#               if quant.unit.name == "dimensionless":
#                   print("DIMENSIONLESS")
#               else:
#                   unitList.append(str(quant.unit.name))

#           print("INGREDIENT:", ingredient, "UNITS", unitList)
#           clean_ingredients.append(deleteUnits(ingredient, unitList))
#       except:
#           pass

# print(sample_ingredients)
# print(clean_ingredients)
# print(l.NAMES["teaspoon"])
# for key in l.NAMES.keys():
#   if not l.NAMES[key].symbols:
#       print("FOUND!", key)
# print(l.NAMES["microbar"].symbols)