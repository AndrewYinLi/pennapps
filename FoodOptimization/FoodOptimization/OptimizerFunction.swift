//
//  OptimizerFunction.swift
//  FoodOptimization
//
//  Created by Mathewe on 9/9/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import Foundation

class Optimizer {
    
    static var ingredients: [Any?] = []
    static var dayList:[Any?] = []
    
    //quantity(list of lists), image, name, yield, content(ingredients)
    func optimize(recipes: [Any?], days: [Any?]) {
        for day in days {
            
            
            if day.B == nil && day.L == nil && day.D == nil {
                continue
            }

            else {
                if day.B != nil {
                    var BRecipe = findRecipe(day.B.number)
                    dayList[day.name].append(BRecipe)
                }
                
                if day.L != nil {
                    var LRecipe = findRecipe(day.L.number)
                    dayList[day.name].append(LRecipe)
                }
                
                if day.D != nil {
                    var DRecipe = findRecipe(day.D.number)
                    dayList[day.name].append(DRecipe)
                }
            }
            
        }
    }
    
    func findRecipe(numPeople: Int) {
        
        
    }
    
    
    func filterRecipes(recipes: [Any?], blackListIngredients: [String]) -> [Any?] { //Returns a list of recipes
        
        
        
        
        return [Any?]()
    }
}



