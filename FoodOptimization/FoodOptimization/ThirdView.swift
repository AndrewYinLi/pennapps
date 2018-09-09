//
//  ThirdView.swift
//  FoodOptimization
//
//  Created by Mathewe on 9/8/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import UIKit

class ThirdView: UIViewController {
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        DStepper.value = 1
        DStepper.minimumValue = 1
        DStepper.maximumValue = 5
        BStepper.minimumValue = 0
        BStepper.maximumValue = 0
        LStepper.minimumValue = 0
        LStepper.maximumValue = 0
        // Do any additional setup after loading the view.
    }


    static var BNum = 0
    
    static var LNum = 0
    
    static var DNum = 1
    
    static var ChoseB = false
    
    static var ChoseL = false
    
    static var ChoseD = true
    
    
    @IBOutlet var BSwitch: UISwitch!
    
    @IBOutlet var LSwitch: UISwitch!
    
    @IBOutlet var DSwitch: UISwitch!
    
    
    
    @IBOutlet var BreakfastNum: UILabel!
    
    @IBOutlet var LunchNum: UILabel!
    
    @IBOutlet var DinnerNum: UILabel!
    
    @IBOutlet var BStepper: UIStepper!
    
    @IBOutlet var LStepper: UIStepper!
    
    @IBOutlet var DStepper: UIStepper!
    
    
    @IBAction func BSwitched(_ sender: Any) {
        if BSwitch.isOn {
            BStepper.minimumValue = 1
            BStepper.maximumValue = 5
            BStepper.value = 1
            BreakfastNum.text = "1"
            
            ThirdView.ChoseB = true
        } else {
            BStepper.minimumValue = 0
            BStepper.maximumValue = 0
            BStepper.value = 0
            BreakfastNum.text = "0"
            
            ThirdView.ChoseB = false
        }
    }
    
    @IBAction func LSwitched(_ sender: Any) {
        if LSwitch.isOn {
            LStepper.minimumValue = 1
            LStepper.maximumValue = 5
            LStepper.value = 1
            LunchNum.text = "1"
            
            ThirdView.ChoseL = true
        } else {
            LStepper.minimumValue = 0
            LStepper.maximumValue = 0
            LStepper.value = 0
            LunchNum.text = "0"
            
            ThirdView.ChoseL = false
        }
    }
    
    @IBAction func DSwitched(_ sender: Any) {
        
        if DSwitch.isOn {
            DStepper.minimumValue = 1
            DStepper.maximumValue = 5
            DStepper.value = 1
            DinnerNum.text = "1"
            
            ThirdView.ChoseD = true
        } else {
            DStepper.minimumValue = 0
            DStepper.maximumValue = 0
            DStepper.value = 0
            DinnerNum.text = "0"
            
            ThirdView.ChoseD = false
        }
    }
    
    
    @IBAction func IncrementB(_ sender: Any) {
        ThirdView.BNum = Int(BStepper.value)
        BreakfastNum.text = String(Int(BStepper.value))
    }
    
    @IBAction func IncrementL(_ sender: Any) {
        ThirdView.LNum = Int(LStepper.value)
        LunchNum.text = String(Int(LStepper.value))
        
    }
    
    @IBAction func IncrementD(_ sender: Any) {
        ThirdView.DNum = Int(DStepper.value)
        DinnerNum.text = String(Int(DStepper.value))
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
