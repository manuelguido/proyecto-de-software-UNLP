function menuSwitch(n) {
    var subItems = document.getElementsByClassName('subItem');
    var menuItems = document.getElementsByClassName('menuItem');
    var panelTitle = document.getElementById('panel-title');
    
    for(var i = 0; i < subItems.length; i++) {
        subItems[i].style.display = 'none';
        menuItems[i].style.background = '#fff';
        menuItems[i].style.color = '#121212';
    }
    panelTitle.innerHTML = menuItems[n].innerHTML;
    subItems[n].style.display = 'block';
    menuItems[n].style.background = '#ddd';
}

function showAddNote() {
    var newNote = document.getElementById('add-note');
    newNote.style.display = "block";
}