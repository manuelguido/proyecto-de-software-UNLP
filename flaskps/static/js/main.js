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

//Toggle de menu del panel de administración
function panelToggle() {
    function switchIcon(){
        var button = document.getElementById("panel-toggle");
        if (button.classList.contains("fa-bars")){
            button.classList.remove("fa-bars");
            button.classList.add("fa-arrow-left");
        }
        else {
            button.classList.remove("fa-arrow-left");
            button.classList.add("fa-bars");
        }
    }
    
    var menu = document.getElementById("panel-menu");
    var smenu = document.getElementById("panel-menu-inner");
    if (menu.classList.contains('hide')) {
        menu.classList.remove("hide");
        smenu.classList.remove("display-n");
    }
    else{
        menu.classList.add("hide");
        smenu.classList.add("display-n");
    }
    switchIcon();
}