function toggleEditForm() {
    var formContainer = document.querySelector('.edit-profile-form-container');
    var editbtn = document.getElementById('edit-btn');

    if (formContainer.style.display === 'none') {
        formContainer.style.display = 'block';
    } else {
        formContainer.style.display = 'none';
    }

    if(editbtn.style.display === 'none') {
        editbtn.style.display = 'block';
    } else {
        editbtn.style.display = 'none';
    }
}