// name input form
const nameChangeForm = document.querySelector('#rename-plant-form');
let plantNameInput = document.querySelector('#plantname-input');
const submitButton = document.querySelector('#submit-name');

nameChangeForm.addEventListener('submit', onSubmit);
submitButton.addEventListener('click', (e) => {
    onSubmit(plantNameInput.value)
});

function onSubmit(plantNameInput) {
    // Function Scope Variables
    let plantName = document.getElementById('plantname');
    plantName.innerText = plantNameInput;
}

// create and initialize plant class
let plant = {
    name: '',
    height: 0,
    hunger: 0,
    light: 0,
    thirst: 0
};
