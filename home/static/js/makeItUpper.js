function makeItUpper(fname, lname) {
    var capitalizedFname = fname.charAt(0).toUpperCase() + fname.slice(1);
    var capitalizedLname = lname.charAt(0).toUpperCase() + lname.slice(1);
    return fname + " " + lname;
}
