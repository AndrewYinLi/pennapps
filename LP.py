from cvxopt import matrix, solvers
import numpy as np

solvers.options['show_progress'] = False
negation = -1
def recipeToIngredients(b, A, y):
    map(lambda x:x*negation, b)
    map(lambda z:z*negation, y)
    npb = matrix([b])
    npy = matrix([y])
    sol = solvers.lp(npb, A, npy)
    print('Ingredients', sol['x'])

def ingredientsToRecipe(b, A, y):
    sol = solvers.lp(b,A,y)
    print('recipes', sol['x'])


b = [-4., -5.]
A = matrix([[2., 1., -1., 0.], [1., 2., 0., -1.]])
y = [3., 3., 0., 0.]
# print(sol['x'])
recipeToIngredients(b,A,y)
