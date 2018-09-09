//
//  IngredientViewController.swift
//  FoodOptimization
//
//  Created by Mathewe on 9/8/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import UIKit

class IngredientViewController: UIViewController {
    
    
    @IBOutlet var NavBar: UINavigationItem!
    @IBOutlet var StatusButton: UIBarButtonItem!
    @IBAction func StatusClicked(_ sender: Any) { 
        if StatusButton.title == "Available"{
            StatusButton.title = "To Buy"
            NavBar.title = "Ingredients Owned"
        }
        else {
            StatusButton.title = "Available"
            NavBar.title = "Ingredients to Buy"
        }
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
}
