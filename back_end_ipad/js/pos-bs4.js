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
let online = navigator.onLine;

const receipt = document.querySelector("#receipt");

// [CONTAINER] HTML Elements Array
var buttons = document.getElementsByTagName("button");
console.log(`buttons.toString(): ${buttons.toString()} \
             elem.length(): ${buttons.length}`);

// [CLOSURE] Button Counter 
const btnCounter = ((/*id*/) => {
    // TODO: remove hardcoding initialization
    var counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    console.log(counter.toString());
    
    // TESTING =======
    var counter_v2 = counterInit_v2();
    console.log(counter_v2.toString());
    // ===============
    
    return function(id) {
        if (id === -Infinity /*-99*/) { 
            // counter = [0,0,0,0,0,0,0,0,0,0,0,0,0];
            counterInit(counter);
            console.log(counter.toString());
            
            // TESTING ============
            counter_v2 = counterInit_v2();
            console.log(counter_v2.toString());
            // ====================
            
        } else {
            counter[id - 1]++;
            
            // TESTING =========
            console.log(++counter_v2[id])
            // =================
            
            return counter;
        }
    }
})();

// [FUNCTION] Counter Array Inititalizer
function counterInit(counter) {
    var i,
        buttonsLen = buttons.length;
    for (i = 0; i < buttonsLen; i++) {
        counter[i] = 0;
    }
}

// [TESTING | FUNCTION] Counter Array Inititalizer - VERSION 2.0
function counterInit_v2() {
    var i,
        buttonsLen = buttons.length,
        counter = [];
    for (i = 0; i < buttonsLen; i++) {
        counter[i] = 0;
    }
    return counter;
}

// [TESTING | CLOSURE] UnderDev -- UNTESTED!!!!!!!!
// TODO: TEST!!
// FIXME: func name change <=> function count(), countIncrementer()
/**
 * { USE }
 * ===========================
 * var cM = counterMethods();
 * var counter = cM.init();   // clean array
 * cM.reset(counter);         // clean array
 */
// function counterMethods() {
const counterMethods = () => {
    var i,
        buttonsLen = buttons.length,
        counter = [];
    
    return {
        init: function() {
            for (i = 0; i < buttonsLen; i++) {
                counter[i] = 0;
            }
            return counter;
        },
        reset: function(counter) {
            for (i = 0; i < buttonsLen; i++) {
                counter[i] = 0;
            }
        }
    }
}

// [PROTOTYPE] Menu Item
// TODO: implement counter into prototype (count)
function Item(id, category, name, label, cost, count=null) {
    this.id = id;
    this.category = category;
    this.name = name;
    this.label = label;
    this.cost = cost;
    this.count = count;
    this.info = function() { 
        return `ID: ${this.id}, Category: ${this.category}, Name: ${this.name}, Label: ${this.label}, Cost: $${this.cost.toFixed(2)}, Count: ${this.count}`
    };
}
/*
// Append Prototype
<PrototypeObject>.prototype.<FunctionName> = function() {
  return <ReturnValue>;
};*/

// [FUNCTION] Load Menu Item Objects
// TODO: full implementation
function parseItems() {
    // OBJECTS FOR TESTING <=> Item(id, category, name, label, cost)
    var items = [
        new Item('BK001', 'bkfast', 'Muffin', 'MUFFIN', 2.75),
        new Item('BK002', 'bkfast', 'House Bagel', 'BAGEL', 3.99),
        new Item('BK003', 'bkfast', 'Breakfast Burrito', 'BKFAST BURRITO', 2.80),
        new Item('BK004', 'bkfast', 'Breakfast Sandwich', 'BKFAST SAND', 2.80),
        new Item('BK005', 'bkfast', 'Oatmeal', 'OATMEAL', 1.50),
        new Item('BK006', 'bkfast', 'Yogurt', 'YOGURT', 2.30),
        new Item('HB001', 'bev_hot', 'Coffee', 'COFFEE', 1.99),
        new Item('HB002', 'bev_hot', 'Hot Tea', 'HOT TEA', 1.99),
        new Item('HB003', 'bev_hot', 'Hot Cocoa', 'COCOA', 1.99),
        new Item('CB001', 'bev_cold', 'Aquafina', 'AQUAFINA', 1.00),
        new Item('CB005', 'bev_cold', 'Rockstar', 'ROCKSTAR', 2.80),
        new Item('CB008', 'bev_cold', 'Juice', 'JUICE', 1.87),
        new Item('DE001', 'deli', 'Noodle Cup', 'NOODLE CUP', 1.00),
        new Item('DE002', 'deli', 'Soup', 'SOUP', 2.80),
        new Item('DE003', 'deli', 'Small Salad', 'SMALL SALAD', 2.10),
        new Item('DE004', 'deli', 'Large Salad', 'LARGE SALAD', 5.00),
        new Item('DE005', 'deli', 'Deli Sand', 'DELI SAND', 4.44),
        new Item('DE006', 'deli', 'Fresh Whole Fruit', 'FRESH FRUIT', 1.00),
        new Item('SN006', 'snack', 'Chips Ahoy', 'CHIPS AHOY', 0.75),
        new Item('SN002', 'snack', 'Chips', 'CHIPS', 0.65),
        new Item('SN003', 'snack', 'House Baked Cookie', 'HOUSE COOKIE', 1.64),
        new Item('SN007', 'snack', 'Rice Krispy', 'RICE KRISPY', 0.75),
        new Item('SN008', 'snack', 'Candy', 'CANDY', 0.75),
        new Item('SN010', 'snack', 'Oreo Pie', 'OREO PIE', 2.99),
        new Item('CD001', 'condiment', 'Salsa', 'SALSA', 0.00),
        new Item('CD002', 'condiment', 'Plain Cream Cheese', 'PLAIN CRM CHZ', 0.75),
        new Item('CD003', 'condiment', 'House Cream Cheese', 'CREAM CHEESE', 0.75),
        new Item('CD004', 'condiment', 'Granola', 'GRANOLA', 0.50),
        new Item('CD005', 'condiment', 'Crackers', 'CRACKERS', 0.00),
        new Item('CD006', 'condiment', 'Dressing', 'DRESSING', 0.75)
    ];
    
    var i,
        n = items.length;
    for (i = 0; i < n; i++){
        console.log(`${items[i].info()}`);
    }
    
    populateButtons(items, n);
}

// [FUNCTION] Assign Buttons
// TODO: full implementation
function populateButtons(items, n) {
    var i;
    for (i = 0; i < n; i++) {
        buttons[i].innerText = items[i].label;
    }
}

// // [FUNCTION] Button Clicked
// // TODO: full implementation?? self vs event
// function onClickTestVanilla(btnID, btnName) {
//     let msg = `<br />${btnName}`;
    
//     console.log(`btnID: ${btnID}  btnName: ${btnName} \
//                  counter: ${btnCounter(parseInt(btnID, 10))}`);
    
//     if (online) { $("#receipt").append(msg); } 
//     else { document.getElementById("receipt").innerHTML += msg; }
// }

// // [FUNCTION] Button Clicked (param=event)
// // TODO: full implementation?? self vs !event
// function onClickTestVanillaEvent(event) {
//     let msg = `<br />${event.target.textContent}` ||
//               `<br />${event.target.innerText}`;
    
//     console.log(`event: ${event}  event.target: ${event.target}  \
//                  event.srcElement: ${event.srcElement}`);
//     console.log(`event.target.textContent: ${event.target.textContent} || \
//                  event.target.innerText: ${event.target.innerText}`);
    
//     if (online) { $("#receipt").append(msg); } 
//     else { document.getElementById("receipt").innerHTML += msg; }
// }

// [FUNCTION] UI Button Clicked
// TODO: var or let ?!?!?!
function buttonUIClicked(event) {
    // var eT = event.target,
    //     srcElem = event.srcElement,
    //     eID = event.target.id,
    //     eName = event.target.name,
    //     eText = event.target.innerText,
    //     item = `<br />${event.target.innerText}`;
        
    let eT = event.target,
        srcElem = event.srcElement,
        eID = eT.id,
        eName = eT.name,
        eText = eT.innerText,
        item = `<br />${eText}`,
        count = btnCounter(parseInt(eID, 10));
    
    // DEBUG =========================================================
    console.log(`event.target.id: ${eID}  event.target.name: ${eName}  counter: ${count}`);
    console.log(`event: ${event}  event.target: ${eT}  event.srcElement: ${srcElem}  event.target.innerText: ${eText}`);
    console.log(`Qty: ${"foo"} Item: ${eText} Cost(ea): ${"bar"} Total: ${"foo"}`);
    // ===============================================================
    
    // let clicked_item = `${item} x${btnCounter(eID)}`
    let clicked_item = `${item}`
    
    if (online) { $("#receipt").append(clicked_item); } 
    else { receipt.innerHTML += clicked_item; }
}

// [FUNCTION] Clear Receipt Div
function clearReceipt() {
    if (online) { $("#receipt").html(""); } 
    else { receipt.innerHTML = ""; }
    
    btnCounter(-Infinity);
}

// [FUNCTION] Calculate Bill Total & Output Receipt (test data)
// TODO: full implementation
function calculateTotal() {
    // To be const or not to be const...tiz the ??
    var taxRate = 0.05;
    
    // TESTING ========================================================================================================================
    
    // Test Vars -> Item(id, category, name, label, cost, count)
    var testPrototypeItem_01 = new Item('BK003', 'bkfast', 'Breakfast Burrito', 'BKFAST BURRITO', 2.80, 1),
        testPrototypeItem_02 = new Item('CB001', 'bev_cold', 'Aquafina', 'AQUAFINA', 1.00, 2),
        testPrototypeItem_03 = new Item('DE004', 'deli', 'Large Salad', 'LARGE SALAD', 5.00, 1),
        testPrototypeItem_04 = new Item('SN003', 'snack', 'House Cookie', 'HOUSE COOKIE', 1.64, 2),
        testPrototypeItem_05 = new Item('CD001', 'condiment', 'Salsa', 'SALSA', 0.00, 1),
        testTransSumPrototype = testPrototypeItem_01.count * testPrototypeItem_01.cost 
                              + testPrototypeItem_02.count * testPrototypeItem_02.cost 
                              + testPrototypeItem_03.count * testPrototypeItem_03.cost 
                              + testPrototypeItem_04.count * testPrototypeItem_04.cost 
                              + testPrototypeItem_05.count * testPrototypeItem_05.cost,
        taxDuePrototype = testTransSumPrototype * taxRate,
        totalPrototype = testTransSumPrototype + taxDuePrototype;
    
    // DEBUG ======================================
    console.log(`${testPrototypeItem_01.info()}`);
    console.log(`${testPrototypeItem_02.info()}`);
    console.log(`${testPrototypeItem_03.info()}`);
    console.log(`${testPrototypeItem_04.info()}`);
    console.log(`${testPrototypeItem_05.info()}`);
    // ============================================
    
    // ================================================================================================================================
    
    // Print receipt output
    printReceipt(testPrototypeItem_01, testPrototypeItem_02,
                 testPrototypeItem_03, testPrototypeItem_04,
                 testPrototypeItem_05, testTransSumPrototype,
                 taxRate, taxDuePrototype, totalPrototype);
}

// [FUNCTION] $ Output Receipt Total
// TODO: full implementation
function printReceipt(item01,item02,item03,item04,item05,sum,taxRate,taxDue,total) {
    var totalPlaceholder = `<pre>
    
<b>ARTY'S CAFÉ</b>
            
-- Bill Total --
                 
x${item01.count} ${item01.name}  $ ${item01.cost.toFixed(2)}ea
x${item02.count} ${item02.name}           $ ${item02.cost.toFixed(2)}ea
x${item03.count} ${item03.name}        $ ${item03.cost.toFixed(2)}ea
x${item04.count} ${item04.name}       $ ${item04.cost.toFixed(2)}ea
x${item05.count} ${item05.name}              $ ${item05.cost.toFixed(2)}ea
<b>================================</b>
    SUBTOTAL:        $ ${sum.toFixed(2)}
    (${(taxRate*100).toFixed(0)}%) TAX:        $  ${taxDue.toFixed(2)}
<b>================================</b>
       <b>TOTAL:        $ ${total.toFixed(2)}</b>
           

 <i>HAVE A GREAT DAY!</i></pre>`;
 
    if (online) { $("#receipt").html(totalPlaceholder); }
    else { receipt.innerHTML = totalPlaceholder; }
}

// [CLOSURE] % Disc Button Clicked
// TODO: full implementation``````
function discount() {
    var disc, percent, amountParsed,
        discPercentStr = ["Discount percentage?","50"],
        discDollarStr = ["Discount amount?","2.25"],
        msgPercent /* = `<br />${percent.toFixed(0)}% discount applied` */,      // FIXME: !!!
        msgDollar /* = `<br />$${amountParsed.toFixed(2)} discount applied` */,  // FIXME: !!!
        alertPercent /* = `${percent.toFixed(0)}% discount applied` */,          // FIXME: !!!
        alertDollar /* = `$${amountParsed.toFixed(2)} discount applied` */;      // FIXME: !!!
    
    return {
        percent: function() {
            disc = prompt(discPercentStr[0],discPercentStr[1]);
            
            if (disc != null || disc != "") {
                percent = parseFloat(disc);
                console.log(`percent: ${percent}  disc: ${disc}`);
            }
            // FIXME: me no likie ========================================
            msgPercent = `<br />${percent.toFixed(0)}% discount applied`;
            // ===========================================================
            if (online) { $("#receipt").append(msgPercent); } 
            else { receipt.innerHTML += msgPercent; }
            // FIXME: me no likie ====================================
            alertPercent = `${percent.toFixed(0)}% discount applied`;
            // =======================================================
            alert(alertPercent);
        },
        dollar: function() {
            disc = prompt(discDollarStr[0],discDollarStr[1]);
            
            if (disc != null || disc != "") {
                amountParsed = parseFloat(disc);
                console.log(`amountParsed: ${amountParsed}  disc: ${disc}`);
            }
            // FIXME: me no likie ============================================
            msgDollar = `<br />$${amountParsed.toFixed(2)} discount applied`;
            // ===============================================================
            if (online) { $("#receipt").append(msgDollar); }
            else { receipt.innerHTML += msgDollar; }
            // FIXME: me no likie ========================================
            alertDollar = `$${amountParsed.toFixed(2)} discount applied`;
            // ===========================================================
            alert(alertDollar);
        }
    }
}

const admin = event => {
    console.log(`event: ${event}  \
                 event.target: ${event.target}  \
                 event.target.innerText: ${event.target.innerText}`);
}

const admin_2 = event => console.log(`event: ${event}  \
                                        event.target: ${event.target}  \
                                        event.target.innerText: ${event.target.innerText}`);
