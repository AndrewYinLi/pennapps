import json
from quantulum import parser # Someone else's fork because main branch is broken: https://github.com/sohrabtowfighi/quantulum

fractionsDict = {'¼': '1/4',
  '½': '1/2',
  '¾': '3/4',
  '⅐': '1/7',
  '⅑': '1/9',
  '⅒': '1/10',
  '⅓': '1/3',
  '⅔': '2/3',
  '⅕': '1/5',
  '⅖': '2/5',
  '⅗': '3/5',
  '⅘': '4/5',
  '⅙': '1/6',
  '⅚': '5/6',
  '⅛': '1/8',
  '⅜': '3/8',
  '⅝': '5/8',
  '⅞': '7/8' }

def replaceFractions(ingredientsSplit):
	for i in range(0, len(ingredientsSplit)):
		for fraction in fractionsDict:
			if fraction in ingredientsSplit[i]:
				ingredientsSplit[i] = ingredientsSplit[i].replace(fraction, fractionsDict[fraction])
	return ingredientsSplit

def parseRecipes(recipeJson):
	f = open(recipeJson, "r", encoding="utf-8-sig")
	lines = f.readlines()
	recipes = []
	for line in lines:
		recipe = json.loads(line)
		recipes.append(recipe)

	parsed = [replaceFractions(r["ingredients"].split("\n")) for r in recipes]

	return parsed

def main():
	recipesList = parseRecipes("recipes.json")
	allIngredients = []
	for ingList in recipesList:
		allIngredients.extend(ingList)

	#print(allIngredients)
	for ingredient in allIngredients:
		try:
			quants = parser.parse(ingredient)
		except:
			# We need to manually parse the text
			pass
		if len(quants) > 0:
			try:
				quants = parser.parse(ingredient)
				if quants[0].value == 'dimensionless':
					# We need to manually parse for the object unit (perhaps standardized)
					pass
				else:
					# Make new JSON object
					pass
				print(quants)
				#print(quants[0].unit.name + str(quants[0].value))
			except:
				# We need to manually parse
				pass

if  __name__ =='__main__':
	main()