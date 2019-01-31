
function change_year()  {
    var e = document.getElementById("queen_year");
    var value = e.options[e.selectedIndex].value;
    var qyear = value % 5;

    var cl = e.classList;
    var ocl;

    for(i=0; i<cl.length; i++)  {
        if ( cl.item(i).substring(0, 4) == "year")
          ocl = cl.item(i);
    }


    e.classList.remove(ocl)

    var ncl;

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

    // e.classList.add("text-s1");
    e.classList.add(ncl);

}


function checkdata()  {
    var is_valid = true;
    var msg = "";

    var hlbl = document.getElementById('hive_label');
    if (hlbl.value.length < 1)  {
        is_valid = false;
        msg += '"Hive Label" is required\n';
    }

    var loc = document.getElementById('location');
    if (loc.value.length < 1)  {
        is_valid = false;
        msg += '"Location" is required\n';
    }

    var bb = document.getElementById('brood_boxes');
    if ( bb.value < 1)  {
        is_valid = false;
        msg += 'number of Brood Boxes must be greater than 1\n';
    }

    var s = document.getElementById('supers');
    if ( s.value < 0)  {
        is_valid = false;
        msg += 'number of Supers must be positive\n'; 
    }

    if ( !is_valid)  {
        alert(msg);
    }

    return is_valid;
}
