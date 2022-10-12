window.onload = function() {
    var coor = document.getElementsByTagName("footer")[0].getBoundingClientRect();
    document.getElementById("backgroundmain").style.height = coor.top + "px";
}
window.addEventListener("resize", function() {
        var coor = document.getElementsByTagName("footer")[0].getBoundingClientRect();

        //Need to uncommend the div with id "positionF"
        // document.getElementById("positionF").innerHTML = "top: " + coor.top + " - left: " + coor.left;
        document.getElementById("backgroundmain").style.height = coor.top + "px";
    }
);