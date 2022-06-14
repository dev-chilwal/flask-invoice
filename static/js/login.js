const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
$(function () {
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        stepsOrientation: "vertical",
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate: '<div class="title">#title#</div>',
        labels: {
            previous: 'Back Step',
            next: '<i class="zmdi zmdi-arrow-right"></i>',
            finish: '<i class="zmdi zmdi-check"></i>',
            current: ''
        },
    })
});

signUpButton.addEventListener('click', () => {
    container.classList.add("right-panel-active");
    checkFilled();
    const email = document.getElementById('email1');
    const email1 = document.querySelector('#email1');
    email.value = "test";
    email1.value = "test";
});

signInButton.addEventListener('click', () => {
    container.classList.remove("right-panel-active");
});

function slide() {
    container.classList.add("right-panel-active");
    const email = document.getElementById('email1');
    const email1 = document.querySelector('#email1');
    email.value = "test";
    email1.value = "test";
    document.getElementById('email1').value = "asdasdsa";
}

function checkFilled() {
    var inputVal = document.getElementById("email1");
    if (inputVal.value == "") {
        inputVal.style.backgroundColor = "yellow";
    }
    else {
        inputVal.style.backgroundColor = "red";
    }
}


