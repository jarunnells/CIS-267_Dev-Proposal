"use strict";

// ==========================================================================
//
//   Developer: J.A. Runnells
//     Updated: 2020-08-15 03:20
//   Last Push: 2020-08-15 03:20
//      Branch: dev-branch
//     License: {PLACEHOLDER}
//
// ==========================================================================

/**
 * dev/code/ProjectsUnderDev/Artys/html/admin.html
 */

// Item Class
class Item {
    constructor(id, category, name, label, price) {
        this.id = id;
        this.category = category;
        this.name = name;
        this.label = label;
        this.price = price;
    }
}

// UI Class
class UI {
    static displayItems() {
        const StoredItems = [
            // BREAKFAST ITEMS
            { "id": "BK001", "category": "bkfast", "name": "Muffin", "label": "MUFFIN", "price": 2.75, },
            { "id": "BK002", "category": "bkfast", "name": "Oatmeal", "label": "OATS", "price": 2.85, },
            { "id": "BK003", "category": "bkfast", "name": "Breakfast Burrito", "label": "B-BURRITO", "price": 2.80, },
            { "id": "BK004", "category": "bkfast", "name": "Breakfast Sandwich", "label": "B-SAND", "price": 2.80, },
            { "id": "BK005", "category": "bkfast", "name": "Bagel", "label": "BAGEL", "price": 1.50, },
            { "id": "BK006", "category": "bkfast", "name": "Yogurt", "label": "YOGURT", "price": 2.30, },
            // HOT BEVERAGES
            { "id": "HB001", "category": "bev_hot", "name": "Coffee", "label": "COFFEE", "price": 1.99, },
            { "id": "HB002", "category": "bev_hot", "name": "Hot Tea", "label": "HOT TEA", "price": 1.99, },
            { "id": "HB003", "category": "bev_hot", "name": "Hot Cocoa", "label": "COCOA", "price": 1.99, },
            // COLD BEVERAGES
            { "id": "CB001", "category": "bev_cold", "name": "Aquafina", "label": "AQUAFINA", "price": 1.00, },
            { "id": "CB002", "category": "bev_cold", "name": "Life Water", "label": "LIFE H20", "price": 1.87, },
            { "id": "CB003", "category": "bev_cold", "name": "Sobe", "label": "SOBE", "price": 2.34, },
            { "id": "CB004", "category": "bev_cold", "name": "5hr Energy", "label": "5 HOUR", "price": 2.80, },
            { "id": "CB005", "category": "bev_cold", "name": "Rockstar", "label": "ROCK⭐️", "price": 2.80, },
            { "id": "CB006", "category": "bev_cold", "name": "Milk", "label": "MILK", "price": 1.87, },
            { "id": "CB007", "category": "bev_cold", "name": "Chocolate Milk", "label": "CHOC MILK", "price": 1.87, },
            { "id": "CB008", "category": "bev_cold", "name": "Juice", "label": "JUICE", "price": 1.87, },
            // FRESH DELI ITEMS
            { "id": "DE001", "category": "deli", "name": "Noodle Cup", "label": "NOODLE CUP", "price": 1.00, },
            { "id": "DE002", "category": "deli", "name": "Soup", "label": "SOUP", "price": 2.80, },
            { "id": "DE003", "category": "deli", "name": "Small Salad", "label": "SM SALAD", "price": 2.10, },
            { "id": "DE004", "category": "deli", "name": "Large Salad", "label": "LG SALAD", "price": 5.00, },
            { "id": "DE005", "category": "deli", "name": "Deli Sand", "label": "DELI SAND", "price": 4.44, },
            { "id": "DE001", "category": "deli", "name": "Fresh Whole Fruit", "label": "FRESH FRUIT", "price": 1.00, },
            { "id": "DE002", "category": "deli", "name": "Fruit Cup", "label": "FRUIT CUP", "price": 2.30, },
            { "id": "DE003", "category": "deli", "name": "Hummus", "label": "HUMMUS", "price": 2.69, },
            { "id": "DE004", "category": "deli", "name": "Guacamole", "label": "GUAC", "price": 2.69, },
            { "id": "DE005", "category": "deli", "name": "String Cheese", "label": "STRING CHZ", "price": 0.75, },
            { "id": "DE006", "category": "deli", "name": "Veggies Snack Pack", "label": "VEGGIES", "price": 1.49, },
            { "id": "DE007", "category": "deli", "name": "Sargento Snack Pack", "label": "SARGENTO", "price": 1.49, },
            // SNACK ITEMS
            { "id": "SN001", "category": "snack", "name": "House Cookie", "label": "HOUSE COOKIE", "price": 1.64, },
            { "id": "SN008", "category": "snack", "name": "Chips", "label": "CHIPS", "price": 0.65, },
            { "id": "SN009", "category": "snack", "name": "House Baked Cookie", "label": "HOUSE COOKIE", "price": 1.64, },
            { "id": "SN010", "category": "snack", "name": "Oreo Cookie", "label": "OREO COOKIES", "price": 0.75, },
            { "id": "SN011", "category": "snack", "name": "M&M Cookie", "label": "M&M COOKIE", "price": 0.75, },
            { "id": "SN012", "category": "snack", "name": "Chips Ahoy", "label": "CHIPS AHOY", "price": 0.75, },
            { "id": "SN013", "category": "snack", "name": "Rice Krispy", "label": "RICE KRISPY", "price": 0.75, },
            { "id": "SN014", "category": "snack", "name": "Candy", "label": "CANDY", "price": 0.75, },
            { "id": "SN015", "category": "snack", "name": "Kind Bar", "label": "KIND BAR", "price": 2.49, },
            { "id": "SN016", "category": "snack", "name": "Oreo Pie", "label": "OREO PIE", "price": 2.99, },
            // CONDIMENTS / SIDES
            { "id": "CD001", "category": "condiment", "name": "Salsa", "label": "SALSA", "price": 0.00, },
            { "id": "CD002", "category": "condiment", "name": "Plain Cream Cheese", "label": "PLAIN CRM CHZ", "price": 0.75, },
            { "id": "CD003", "category": "condiment", "name": "House Cream Cheese", "label": "HOUSE CRM CHZ", "price": 0.75, },
            { "id": "CD004", "category": "condiment", "name": "Granola", "label": "GRANOLA", "price": 0.50, },
            { "id": "CD005", "category": "condiment", "name": "Crackers", "label": "CRACKERS", "price": 0.00, },
            { "id": "CD006", "category": "condiment", "name": "Dressing", "label": "DRESSING", "price": 0.75, },
        ];
        
        const items = StoredItems;
        // TODO: LOCAL STORAGE implementation [remove hard-coded and implement local storage fully]
        //const itemsNEW = Store.getItems();
        
        items.forEach((item, index) => UI.addItemToList(item, index));
    }
    
    static addItemToList(item,index) {
        const list = document.querySelector("#item-list");
        
        const row = document.createElement("tr");
        
        row.innerHTML = `
            <td>${index+1}</td>
            <td>${item.id}</td>
            <td>${item.category}</td>
            <td>${item.name}</td>
            <td>${item.label}</td>
            <td>$ ${parseFloat(item.price, 10).toFixed(2)}</td>
            <td></td>
            <td>
                <a href="#" class="btn btn-success btn-sm update"><i class="material-icons" style="font-size:12px">update</i></a>
                <a href="#" class="btn btn-danger btn-sm delete"><i class="material-icons" style="font-size:12px">delete</i></a>
            </td>
        `;
        
        list.appendChild(row);
    }
    
    static updateItem(elem) {
        if (elem.classList.contains("update")) {
            console.log("UPDATE clicked!");
        }
    }
    
    static deleteItem(elem) {
        if (elem.classList.contains("delete")) {
            elem.parentElement.parentElement.remove();
        }
    }
    
    static showAlert(msg, clsName) {
        const div = document.createElement("div");
        div.className = `alert alert-${clsName}`;
        div.appendChild(document.createTextNode(msg));
        const container = document.querySelector(".container");
        const form = document.querySelector("#item-form");
        container.insertBefore(div, form);
        
        // Vanish alert
        setTimeout(() => document.querySelector(".alert").remove(), 3000);
    }
    
    static clearFields() {
        document.querySelector("#itemID").value = "";
        document.querySelector("#category").value = "";
        document.querySelector("#name").value = "";
        document.querySelector("#label").value = "";
        document.querySelector("#price").value = "";
    }
}

// Storage Class
class Store {
    static getItems() {
        let items;
        if (localStorage.getItem("items") === null) {
            items = [];
        } else {
            items = JSON.parse(localStorage.getItem("items"));
        }
        return items;
    }
    
    static addItem(item) {
        const items = Store.getItems();
        items.push(item);
        localStorage.setItem("items", JSON.stringify(items));
    }
    
    static removeItem(itemID) {
        const items = Store.getItems();
        
        items.forEach((item, index) => {
            if (item.itemID === itemID) {
                items.splice(index,1);
            }
        });
        
        localStorage.setItem("items", JSON.stringify(items));
    }
}

function toggleElemByID(id) {
    const elem = document.querySelector(id);
    if (elem.style.display === "none") {
        elem.style.display = "inherit";
    } else {
        elem.style.display = "none";
    }
}

/**
 * EVENTS
 */
const form = document.querySelector("#item-form");

// Display items
document.addEventListener("DOMContentLoaded", UI.displayItems);

// Add item top list
form.addEventListener("submit", (e) => {
    // Prevent default submit behavior
    e.preventDefault();
    
    // Get form values
    const itemID = document.querySelector("#itemID").value;
    const category = document.querySelector("#category").value;
    const name = document.querySelector("#name").value;
    const label = document.querySelector("#label").value;
    const price = document.querySelector("#price").value;
    
    // Validate form values
    if (itemID === "" || category === "" || name === "" || label === "" || price === "") {
        UI.showAlert("All Fields Required!","danger");
    } else {
        // Instantiate Item
        const item = new Item(itemID, category, name, label, price);
        
        // Add item to UI
        UI.addItemToList(item);
        
        // Add item to local storage
        Store.addItem(item);
        
        // Show item added successfully alert
        UI.showAlert("Item Added Successfully!", "success");
        
        // Clear fields
        UI.clearFields();
    }
});

// Toggle Add Item Form
//form.addEventListener("click", listener, useCapture)

// Form Input Highlighting
document.querySelector("#bal-form, #item-form").addEventListener("focus", (e) => {
    document.querySelector(".form-control").style.backgroundColor = "lightyellow";
    const Inputs = document.querySelectorAll(".form-control");
    
    Inputs.forEach((input, index) => {
        console.log(`input.id: ${input.id} index: ${index}`);
    });
    
    console.log(Inputs);
    console.log(`e.target.id: ${e.target.id}`);
}, true);
document.querySelector("#bal-form, #item-form").addEventListener("blur", (e) => {
    document.querySelector(".form-control").style.backgroundColor = "";
}, true);

// Remove item from list
document.querySelector("#item-list").addEventListener("click", (e) => {
    
    if (e.target.classList.contains("delete")) {
        if (confirm(`Confirm Remove Item?`)) {
            // Remove item from UI
            UI.deleteItem(e.target);
            
            // Remove item from local storage
            Store.removeItem(e.target.parentElement.previousElementSibling.textContent);
            
            // Show item removed successfully alert
            UI.showAlert("Item Removed Successfully!","success");
        }
        // // Remove item from UI
        // UI.deleteItem(e.target);
        
        // // Remove item from local storage
        // Store.removeItem(e.target.parentElement.previousElementSibling.textContent);
        
        // // Show item removed successfully alert
        // UI.showAlert("Item Removed Successfully!","success");
    } else if (e.target.classList.contains("update")) {
        // DEBUG alert
        UI.showAlert("Item Update Clicked!","warning");
    }
    
    // // Remove item from UI
    // UI.deleteItem(e.target);
    
    // // Remove item from local storage
    // Store.removeItem(e.target.parentElement.previousElementSibling.textContent);
    
    // // Show item removed successfully alert
    // UI.showAlert("Item Removed Successfully!","success");
});