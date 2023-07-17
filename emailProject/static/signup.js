const form = document.getElementById('form');
const email = document.getElementById('email');
const fname = document.getElementById('fname');
const lname = document.getElementById('lname');
const age = document.getElementById('age');
const submitButton = document.getElementById('button_submit');

submitButton.disabled

form.addEventListener('submit', e => {
    e.preventDefault();
    validateInputs();
});

const setError = (element, message) => {
    const cntrl = element.parentElement;
    const errorDisplay = cntrl.querySelector('.error');

    errorDisplay.innerText = message;
    cntrl.classList.add('error');
    cntrl.classList.remove('success');
};

const setSuccess = element => {
    const cntrl = element.parentElement;
    const errorDisplay = cntrl.querySelector('.error');

    errorDisplay.innerText = '';
    cntrl.classList.add('success');
    cntrl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    return re.test(String(email).toLowerCase());
};

const validateInputs = () => {
    const emailValue = email.value.trim();
    const ageValue = parseInt(age.value.trim(), 10);
    const fnameValue = fname.value.trim();
    const lnameValue = lname.value.trim();

    if (fnameValue === "") {
        setError(fname, "First Name is required");
    } else if (fnameValue.length < 3 || fnameValue.length > 20 || /\d/.test(fnameValue) || /[\d\W]/.test(fnameValue)) {
        setError(fname, "First Name must be between 3 and 20 characters and should not contain numbers");
    } else {
        setSuccess(fname);
    }

    if (lnameValue === "") {
        setError(lname, "Last Name is required");
    } else if (lnameValue.length < 3 || lnameValue.length > 25 || /\d/.test(lnameValue) || /[\d\W]/.test(lnameValue)) {
        setError(lname, "Last Name must be between 3 and 25 characters and should not contain numbers");
    } else {
        setSuccess(lname);
    }

    if (ageValue <= 0 || isNaN(ageValue) || ageValue >= 100) {
        setError(age, "Invalid Age");
    } else {
        setSuccess(age);
    }

    if (emailValue === "") {
        setError(email, "Email is required");
    } else if (!isValidEmail(emailValue)) {
        setError(email, "Make sure that is your correct name.");
    } else {
        setSuccess(email);
    }
    const inputs = document.querySelectorAll('.cntrl input');
    const isValid = Array.from(inputs).every(input => input.parentElement.classList.contains('success'));

    submitButton.disabled = !isValid;
};
// Add event listeners to input fields
email.addEventListener('input', validateInputs);
fname.addEventListener('input', validateInputs);
lname.addEventListener('input', validateInputs);
age.addEventListener('input', validateInputs);