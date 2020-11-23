"use strict";

const greet = () => {
    let name = prompt_name();
    let msg = create_greeting(name);
    document.querySelector("#greet").innerHTML = msg;
};

const prompt_name = () => {
    return prompt("Name:", "Your name...");
};

const create_greeting = name => {
    if (name == null || name == "") {
        return "Prompt cancelled!";
    } else {
        return `Greetings ${name}!`;
    }
};

document.addEventListener("DOMContentLoaded", event => {
    greet();
});