//
//  IngCollectionViewController.swift
//  FoodOptimization
//
//  Created by Jane Hsieh on 9/9/18.
//  Copyright © 2018 Jane Hsieh. All rights reserved.
//

import UIKit

private let reuseIdentifier = "Cell"

class IngCollectionViewController: UICollectionViewController,
    UINavigationControllerDelegate{
    
//    @IBAction func ChangeStatus(_ sender: Any) {
//    }
    var executeOnce = true
    var cellDimensions = [String:Int]()
    var cellHeight = 50
    var cellWidth = 120
    
    var collectionContainerView: UICollectionView!
    var navBar: UINavigationBar = UINavigationBar()
    
    
    // view constants
    var viewY = CGFloat()
    var viewX = CGFloat()
    var viewWidth = CGFloat()
    var viewHeight = CGFloat()
    
    
    // gaps from view edge
    let leftGap = CGFloat(20)
    let rightGap = CGFloat(20)
    
    
    // navbar constants
    let navBarHeight = CGFloat(64)
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
        navBar.backgroundColor = UIColor.green
        executeOnce = true
        viewY = view.frame.origin.y
        viewX = view.frame.origin.x
        viewWidth = view.frame.width
        viewHeight = view.frame.height
    }
    
    
    override func viewDidAppear(_ animated: Bool) {
        configureCollectionView()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        self.collectionView!.register(UICollectionViewCell.self, forCellWithReuseIdentifier: reuseIdentifier)

        // Dispose of any resources that can be recreated.
    }

    override func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 2
    }

    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath) as! IngredientCollectionViewCell
        cell.Name.text = "Apples"
        return cell
    }
    
    

    /*
    // Uncomment this method to specify if the specified item should be highlighted during tracking
    override func collectionView(_ collectionView: UICollectionView, shouldHighlightItemAt indexPath: IndexPath) -> Bool {
        return true
    }
    */

    /*
    // Uncomment this method to specify if the specified item should be selected
    override func collectionView(_ collectionView: UICollectionView, shouldSelectItemAt indexPath: IndexPath) -> Bool {
        return true
    }
    */

    /*
    // Uncomment these methods to specify if an action menu should be displayed for the specified item, and react to actions performed on the item
    override func collectionView(_ collectionView: UICollectionView, shouldShowMenuForItemAt indexPath: IndexPath) -> Bool {
        return false
    }

    override func collectionView(_ collectionView: UICollectionView, canPerformAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?) -> Bool {
        return false
    }

    override func collectionView(_ collectionView: UICollectionView, performAction action: Selector, forItemAt indexPath: IndexPath, withSender sender: Any?) {
    
    }
    */

}
