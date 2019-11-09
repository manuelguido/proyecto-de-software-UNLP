//Cambia las opciones del menu
function menuSwitch(n) {
    var subItems = document.getElementsByClassName('subItem');
    var menuItems = document.getElementsByClassName('menuItem');
    var panelTitle = document.getElementById('panel-title');
    
    for(var i = 0; i < subItems.length; i++) {
        subItems[i].style.display = 'none';
        menuItems[i].classList.remove("menuItemActive");
    }
    panelTitle.innerHTML = menuItems[n].innerHTML;
    menuItems[n].classList.add("menuItemActive");
    subItems[n].style.display = 'block';
}

function showAddNote() {
    var newNote = document.getElementById('add-note');
    newNote.style.display = "block";
}
