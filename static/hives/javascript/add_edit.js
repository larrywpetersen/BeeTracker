

// Handle change to hive from field

function change_from()  {
    var qf = document.getElementById("queen_from");
    if( qf.value.length == 0 )  {
        var hf = document.getElementById("hive_from");
        qf.value = hf.value;
    }
}


// Change the color of the Queen Year to match the new year

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


// Check to see if the label is unique

var label_is_unique = true;

var xmlhttp_label_unique = new XMLHttpRequest();

xmlhttp_label_unique.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var answer = JSON.parse(this.responseText);
        do_is_label_unique(answer);
    }
};

function is_label_unique()  {
    var label = document.getElementById("hive_label").value;
    var url = "../is_hive_label_unique/?label=" + label;
    xmlhttp_label_unique.open("GET", url, true);
    xmlhttp_label_unique.send();
}

function do_is_label_unique(answer) {
    label_is_unique = answer[0].unique;
    if (label_is_unique)  {
        // document.getElementById("unique-message").innerHTML =
        // '<font color="green">label is unique</font>';
    }  else  {
        document.getElementById("unique-message").innerHTML =
            '<font color="red">label is not unique</font>';
    }
}


// Validate Form Data

function checkdata()  {
    var is_valid = true;
    var msg = "";

    var hlbl = document.getElementById('hive_label');
    if (hlbl.value.length < 1)  {
        is_valid = false;
        msg += '"Hive Label" is required\n';
    }

    if ( ! label_is_unique )  {
        is_valid = false;
        msg += '"Hive Label" must be unique\n';
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
