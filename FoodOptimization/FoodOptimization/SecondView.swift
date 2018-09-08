//
//  SecondView.swift
//  FoodOptimization
//
//  Created by Mathewe on 9/8/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import UIKit

class SecondView: UIViewController, UITableViewDelegate {
    
    @IBOutlet weak var displayName: UILabel!
    var myString = String()
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        displayName.text = myString
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
  
}
