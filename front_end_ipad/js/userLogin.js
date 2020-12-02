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
 * dev/code/ProjectsUnderDev/Artys/index.html
 */
 

const btn = document.querySelector("#ulogin");
btn.addEventListener("click", (e) => {
    e.preventDefault();
    const user = document.querySelector("#username").value;
    const pass = document.querySelector("#pwd").value;
    const admin = "html/admin.html";
    
    if (user.toLowerCase() === "admin" && pass === "12345") {
        alert("User credentials validated!");
        window.location = admin;
    } else {
        alert("Invalid user credentials!");
    }
    
});

// USER and PASS HASHING....
// Vanilla .js
// Convert to 32bit integer 
// function stringToHash(str) { 
      
//     var hash = 0,
//         len = str.length; 
      
//     if (len == 0) return hash; 
      
//     for (let i = 0; i < len; i++) { 
//         char = str.charCodeAt(i); 
//         hash = ((hash << 5) - hash) + char; 
//         hash = hash & hash; 
//     }
//     return hash; 
// } 
  
// // String printing in hash 
// let user = "admin",
//     pass = "12345";

// console.log(`userHash: ${stringToHash(user)}  passHash: ${stringToHash(pass)}`);


// // Node.js
// // Importing 'crypto' module 
// const crypto = require('crypto'), 

// // Returns the names of supported hash algorithms  
// // such as SHA1,MD5 
// let hash = crypto.getHashes();

// // Create hash of SHA1 type 
// let user = "admin",
//     pass = "12345";

// // 'digest' is the output of hash function containing  
// // only hexadecimal digits 
// let hashUsr = crypto.createHash('sha1').update(user).digest('hex');
// //let hashPas = crypto.createHash('sha1').update(pass).digest('hex');

// console.log(hash);