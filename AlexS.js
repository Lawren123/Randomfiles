function myFunction() {
    document.body.style.background = "#000000 url('ABCmyth.jpg') no-repeat right top";
}

function openCreature(evt, creatureName) {
                  var i, tabcontent, tablinks;
                  tabcontent = document.getElementsByClassName("tabcontent");
                  for (i = 0; i < tabcontent.length; i++) {
                      tabcontent[i].style.display = "none";
                  }
                  tablinks = document.getElementsByClassName("tablinks");
                  for (i = 0; i < tablinks.length; i++) {
                      tablinks[i].className = tablinks[i].className.replace(" active", "");
                  }
                  document.getElementById(creatureName).style.display = "block";
                  evt.currentTarget.className += " active";
              }


function openCity(evt, creatureName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(creatureName).style.display = "block";
    evt.currentTarget.className += " active";
}
