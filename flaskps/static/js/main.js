function validateStrings() {
    var strs = document.getElementsByClassName('string');
    for (let index = 0; index < strs.length; index++) {
        strs[index].value = strs[index].value.trim();
    }
    for (let index = 0; index < strs.length; index++) {
        if (strs[index].value = ""){
            return false;
        }
    }
}