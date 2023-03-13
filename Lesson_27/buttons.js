const myDiv = document.createElement("div");
myDiv.className = 'buttons';
myDiv.style.background = 'white';
myDiv.style.textAlign = 'center';

['Button 1', 'Button 2', 'Button 3'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'Button';
    button.innerText = buttonName;
    button.style.marginLeft = '5px'
    button.style.marginRight = '5px'
})

document.getElementsByTagName('body')[0].appendChild(myDiv);