function greetButton() {
    const name= document.getElementById("name").value;
    const greetingMessage= document.getElementById("greetingMessage");
    greetingMessage.textContent= "Hello, " + name + ", I hope you are having a wonderful day!";
}