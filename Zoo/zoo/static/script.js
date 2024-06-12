//****************************************************************
//here are functions handling EMPLOYEES
function edit_employee(id) {
    sel = window.prompt("Which name do you want to edit?", "first/last");
    new_name = window.prompt("Choose new name: ", "New name");
    if (new_name != null && new_name != "") {
        var response = fetch('http://127.0.0.1:443/back/edit-employee', {
          method: 'PUT',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id,
            'SEL': sel
          },
          body: new_name
        });
    }
}

function add_employee() {
    first_name = document.getElementById('first-name').value
    last_name = document.getElementById('last-name').value
    if (first_name != null && first_name != "" && last_name != null && last_name != "") {
        var response = fetch('http://127.0.0.1:443/back/add-employee', {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'FN': first_name,
            'LN': last_name
          }
        });
    }
}

function remove_employee(id) {
    confirm = window.confirm("Are you sure?");
    if (confirm) {
        var response = fetch('http://127.0.0.1:443/back/remove-employee', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id
          }
        });
    }
}

//****************************************************************
//here are functions handling ANIMALS
function edit_animal(id) {
    sel = window.prompt("Which property do you want to edit?", "name/species/enclosure");
    new_value = window.prompt("Choose new value: ", "New value");
    if (new_value != null && new_value != "") {
        var response = fetch('http://127.0.0.1:443/back/edit-animal', {
          method: 'PUT',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id,
            'SEL': sel
          },
          body: new_value
        });
    }
}

function add_animal() {
    name = document.getElementById('name').value
    species = document.getElementById('species').value
    enclosure = document.getElementById('enclosure').value
    if (name != null && name != "" && species != null && species != "") {
        var response = fetch('http://127.0.0.1:443/back/add-animal', {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'NM': name,
            'SP': species,
            'ENC':enclosure
          }
        });
    }
}

function remove_animal(id) {
    confirm = window.confirm("Are you sure?");
    if (confirm) {
        var response = fetch('http://127.0.0.1:443/back/remove-animal', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id
          }
        });
    }
}


//****************************************************************
//here are functions handling ENCLOSURES
function edit_enclosure(id) {
    sel = window.prompt("Which property do you want to edit?", "location/inhabitant");
    new_value = window.prompt("Choose new value: ", "New value");
    if (new_value != null && new_value != "") {
        var response = fetch('http://127.0.0.1:443/back/edit-enclosure', {
          method: 'PUT',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id,
            'SEL': sel
          },
          body: new_value
        });
    }
}

function add_enclosure() {
    location = document.getElementById('location').value
    inhabitant = document.getElementById('inhabitant').value
    if (location != null && location != "") {
        var response = fetch('http://127.0.0.1:443/back/add-enclosure', {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'LC': location,
            'INH': inhabitant
          }
        });
    }
}

function remove_enclosure(id) {
    confirm = window.confirm("Are you sure?");
    if (confirm) {
        var response = fetch('http://127.0.0.1:443/back/remove-enclosure', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id
          }
        });
    }
}

