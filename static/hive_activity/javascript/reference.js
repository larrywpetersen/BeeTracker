

change_year();

function change_year()  {
    var e = document.getElementById("year");
    var value = e.options[e.selectedIndex].value;
    var qyear = value % 5;

    var ocl = e.classList.item(0);

    var ncl;

    e.classList.remove(ocl)
    if (qyear == 0) {
        ncl = "year0";
    }
    else if (qyear == 1) {
        ncl = "year1";
    }
    else if (qyear == 2) {
        ncl = "year2";
    }
    else if (qyear == 3) {
        ncl = "year3";
    }
    else if (qyear == 4) {
        ncl = "year4";
    }
    else {
        ncl = "yearx";
    }

    e.classList.add(ncl);

}
