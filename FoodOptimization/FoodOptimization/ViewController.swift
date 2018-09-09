//
//  ViewController.swift
//  FoodOptimization
//
//  Created by Jane Hsieh on 9/8/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet var inputName: UITextField!
    static var userName = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        inputName.delegate = self
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    
    
    @IBAction func savePrefs(_ sender: Any) {
        if inputName.text! != "" {
            ViewController.userName = inputName.text!
        } else {
            ViewController.userName = "Stranger"
        }
        self.performSegue(withIdentifier: "mainSegue", sender: self)
    }
    
    
    @IBAction func vegetarian(_ sender: Any) {
    }
    
    @IBAction func pescetarian(_ sender: Any) {
    }
    
    @IBAction func vegan(_ sender: Any) {
    }
    
    @IBAction func gluten(_ sender: Any) {
    }
    
    @IBAction func dairy(_ sender: Any) {
    }
    
    @IBAction func nuts(_ sender: Any) {
    }
    
    
    
}

