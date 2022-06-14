function findTotal() {

    const amts = document.querySelectorAll(".Amount");
    //const total = document.querySelector("#total_fee");
    const total = document.getElementById("total_fee");

    var amt1 = document.getElementById("amt1").value;
    var amt2 = document.getElementById("amt2").value;
    var amt3 = document.getElementById("amt3").value;
    total.value = 0
    if (amt1 > 0) {
        document.getElementById("upload1").disabled = false;
        document.getElementById("upload-photo1").disabled = false;
    } else {
        document.getElementById("upload1").disabled = true;
        document.getElementById("upload-photo1").disabled = true;
    }
    //if (amt2 > 0) {
    //    document.getElementById("upload2").disabled = false;
    //    document.getElementById("file2").disabled = false;
    //} else {
    //    document.getElementById("upload2").disabled = true;
    //    document.getElementById("file2").disabled = true;
    //}
    if (amt3 > 0) {
        document.getElementById("upload3").disabled = false;
        document.getElementById("upload-photo3").disabled = false;
    } else {
        document.getElementById("upload3").disabled = true;
        document.getElementById("upload-photo3").disabled = true;
    }
    console.log(amt1, amt3)
    let sum = 0;
    amts.forEach(amt => {
        if (amt.valueAsNumber) {
            sum += amt.valueAsNumber;
        }
    });
    total.value = sum;
}
function fileNames() {

    var upl1 = document.getElementById("file1");
    console.log(upl1.files[0].mozFullPath)

}

function notEmpty() {

    findTotal();
    var e = document.getElementById("Month");
    var strUser = e.options[e.selectedIndex].value;
    document.getElementById('desc1').value = "Product Reimbursent-".concat(strUser);
    document.getElementById('desc2').value = "Influencer Payout-".concat(strUser);
    document.getElementById('desc3').value = "Travel Expenses-".concat(strUser);

}
$('#invoice').submit(function (e) {
    e.preventDefault();

    // do ajax now
    console.log("submitted");
});

function disableButton() {
    console.log('Button pressed');
    const button = document.getElementById("Submit");
    button.disabled = true;
    button.style.backgroundColor = '#e7e7e7';
    button.value = "Generating Invoice....";
    //document.getElementById('Submit1').click();
    return true;
}
$("invoice").submit(function () {
    console.log('etstseas')
    if ($(this).valid()) {
        $(this).submit(function () {
            return false;
        });
        return true;
    }
    else {
        return false;
    }
});