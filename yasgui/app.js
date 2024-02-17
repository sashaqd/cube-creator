// document.addEventListener("DOMContentLoaded", function() {
 
//     tab = yasgui.getTab();
//     console.log(tab);

// });


document.addEventListener('DOMContentLoaded', function() {
    
    tab = yasgui.getTab(0);
    tabId = tab.persistentJson.id;

    tabDiv = document.querySelector('#tab-' + tabId);

    // Change the tab name
    span = tabDiv.querySelector('span');
    span.textContent = 'Text Query';

    // Hide the close tab button
    closeTabDiv = document.querySelector('#tab-' + tabId + ' .closeTab');
    closeTabDiv.style.display = 'none';


    console.log('box function called');

    // Create and insert the custom box before the yasqeDiv
    const customBox = document.createElement('div');
    customBox.classList.add('custom-box');
    customBox.style.width = '1425px';
    customBox.style.height = '300px';
    customBox.style.padding = '10px';
    customBox.style.marginLeft = '-10px';


    const textBox = document.createElement('input');
    textBox.setAttribute('type', 'text');
    textBox.setAttribute('placeholder', 'Enter text query');
    textBox.style.width = '100%';
    textBox.style.paddingLeft = '40px';

    textBox.style.fontSize = '19px';
    textBox.style.fontFamily = 'Arial, sans-serif';

    textBox.style.height = '100%';
    textBox.style.boxSizing = 'border-box';
    textBox.style.border = '1px solid #ddd';
    
    customBox.appendChild(textBox);
    
    const yasqeDiv = document.querySelector('.yasqe');
    yasqeDiv.parentNode.insertBefore(customBox, yasqeDiv);
   
});

