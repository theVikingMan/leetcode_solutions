import collections

def solution(recipes, ingredients, supplies):
  adjList = collections.defaultdict(list) # hold all of the ingredients and what that are a component of
  inDegress = collections.defaultdict(int) # count for number of ingredients to make that recipe

  for recp, ing in zip(recipes, ingredients): # loop over both the recipe and ingredients
    for i in ing:
      adjList[i].append(recp) # add the recipe that the ingrendent is a part of
      inDegress[recp] += 1 # increase how many ingredients are need to make the recipe

  completed = [] # to solve one recipe built on another

  while supplies: # supplies will act as a stack
    oneIng = supplies.pop() # Analyze an ingredient
    for component in adjList[oneIng]: # for every recipe that the ingrident can make
      inDegress[component] -= 1 # mark that we have one less ingredient to worry about
      if inDegress[component] == 0: # if we have found a recipe that has all ingreidents
        completed.append(component) # Keeps track of completed recipes
        supplies.append(component) # if a recipe is complete its now a supplies
  return completed

print(solution(["bread","sandwich"],[["yeast","flour"],["bread","meat"]],["yeast","flour","meat"]))