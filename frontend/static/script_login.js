
//---------------------------- Functions

function snakeToStandard(snake) {
    return snake.replace(/_/g, ' ').toLowerCase();
}

function validateForm() {
    let isValid = true; // Flag to track form validity

    const formElements = document.querySelectorAll('#loginForm [id]');
    const formElementIds = Array.from(formElements)
    .map(element => element.id)
    .filter(id => !id.includes('error'))
    // only check for "required" elements
    .filter(id => document.getElementById(id).getAttribute('data-required') === 'true');
        
    for (let i in formElementIds) {
        id = formElementIds[i]
        
        // Clear previous error messages
        document.getElementById(id + '-error').textContent = '';

        const element = document.getElementById(id).value
        const id_space = snakeToStandard(id)
        const elementName = id_space.charAt(0).toUpperCase() + id_space.slice(1)
        
        if (element.trim() === '') {
            const errorText = elementName + ' is required.';
            document.getElementById(id + '-error').textContent = (errorText);
            isValid = false; // Set flag to false if invalid
        }
    }

    return isValid;
}

//---------------------------- Execution

// on login-button press
document.getElementById('loginForm').addEventListener(
    'submit', 
    async function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        if (!validateForm()) {
            return;
        }

        const formData = new FormData(this) //get form

        try{ 
            const response = await fetch('/login', {
                method: 'POST',
                body: formData
            });

            if (response.ok){
                window.location.href = '/success'
            } else{
                alert('Login failded!');
            }
        } catch (error) {
            console.error('Error: ', error);
            alert('An error has occured ong...')
        }

});

// empty the input panels after reloading
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('loginForm').reset(); // Reset the form on page load
});
