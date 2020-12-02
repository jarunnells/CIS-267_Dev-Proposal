"use strict";

// ==========================================================================
//
//   Developer: J.A. Runnells
//     Updated: {PLACEHOLDER}
//   Last Push: {PLACEHOLDER}
//      Branch: {PLACEHOLDER}
//     License: {PLACEHOLDER}
//
// ==========================================================================

/**
 * dev/code/ProjectsUnderDev/Artys/html/jsonTest.html
 */

fetch('../assets/data/menuItems.json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log(`error: ${err}`);
    });
    
function appendData(data) {
    var containerStringify = document.querySelector("#json-stringify");
    var containerParsed = document.querySelector("#json-parsed");
    let i,
        n = data.length;
    for (i = 0; i < n; i++) {
        var div = document.createElement("div");
        div.innerHTML = `[${i+1}] `;
        div.innerHTML += `ID: ${data[i].id}, `;
        div.innerHTML += `Category: ${data[i].category}, `;
        div.innerHTML += `Name: ${data[i].name}, `;
        div.innerHTML += `Label: ${data[i].label.toUpperCase()}, `;
        div.innerHTML += `Price: $ ${parseFloat(data[i].price).toFixed(2)}`;
        containerStringify.appendChild(div);
    }
    for (i = 0; i < n; i++) {
        var div = document.createElement("div");
        
    }
}

fetch('../assets/data/menuItems-NEW.json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        appendDataNEW(data);
    })
    .catch(function (err) {
        console.log(`error: ${err}`);
    });
    
function appendDataNEW(data) {
    var containerStringifyNEW = document.querySelector("#json-stringify-NEW");
    var pre = document.createElement("pre");
    var jsonDataNEW = JSON.stringify(data, null, 2);
    pre.innerText = jsonDataNEW;
    containerStringifyNEW.appendChild(pre);
    //jsonString, null, 2
    // containerStringifyNEW.append(data)
}

// ============================================================================
 
// fetch('../assets/data/menuItems.json')
//     .then(function (response) {
//         return response.json();
//     })
//     .then(function (data) {
//         appendData(data);
//     })
//     .catch(function (err) {
//         console.log('error: ' + err);
//     });
    
// function appendData(data) {
//     var mainContainer = document.querySelector("#myData");
//     for (var i = 0; i < data.length; i++) {
//         var div = document.createElement("div");
//         div.innerHTML = 'Name: ' + data[i].firstName + ' ' + data[i].lastName;
//         mainContainer.appendChild(div);
//     }
// }