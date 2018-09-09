//
//  SecondView.swift
//  FoodOptimization
//
//  Created by Mathewe on 9/8/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import UIKit

class SecondView: UIViewController, UITableViewDelegate {
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if SecondView.generatedDays == false {
            generateDays()
            SecondView.generatedDays = true
        }
        DisplayBar.title = "Hello " + ViewController.userName
        // Do any additional setup after loading the view.
    }
    
    
    @IBOutlet var DisplayBar: UINavigationItem!

    static var generatedDays = false
    
    @IBOutlet var Day1: UIButton!
    @IBOutlet var Day2: UIButton!
    @IBOutlet var Day3: UIButton!
    @IBOutlet var Day4: UIButton!
    @IBOutlet var Day5: UIButton!
    @IBOutlet var Day6: UIButton!
    @IBOutlet var Day7: UIButton!
    static var lastClicked = ""
    
    @IBAction func Day1Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day1.titleLabel?.text)!
    }
    
    @IBAction func Day2Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day2.titleLabel?.text)!
    }
    @IBAction func Day3Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day3.titleLabel?.text)!
    }
    
    @IBAction func Day4Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day4.titleLabel?.text)!
    }
    
    @IBAction func Day5Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day5.titleLabel?.text)!
    }
    
    @IBAction func Day6Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day6.titleLabel?.text)!
    }
    
    @IBAction func Day7Clicked(_ sender: Any) {
        SecondView.lastClicked = (Day7.titleLabel?.text)!
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func getDayOfWeek(_ today:String) -> Int? {
        
        let formatter  = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"
        guard let todayDate = formatter.date(from: today) else { return nil }
        let myCalendar = Calendar(identifier: .gregorian)
        let weekDay = myCalendar.component(.weekday, from: todayDate)
        return weekDay
    }
    
    func generateDays() -> Void {
        
        let DayStrings = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        var DayArray = [UIButton]()

        for item in [Day1, Day2, Day3, Day4, Day5, Day6, Day7] {
            DayArray.append(item!)
        }
        
        let date = Date()
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"
        let result = formatter.string(from:date)
        
        let dayIndex = getDayOfWeek(result)! - 1

        for i in 0...6 {
            let currentIndex = (i + dayIndex) % 7
            DayArray[i].setTitle(DayStrings[currentIndex], for: .normal)
        }

    }
    

    
    
}
