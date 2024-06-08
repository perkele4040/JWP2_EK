

function edit_task(id) {
    new_name = window.prompt("Edit task id: " + id,"New name");
    if (new_name != null && new_name != "") {
        var response = fetch('http://127.0.0.1:443/back/edit-task', {
          method: 'POST',
          headers: {
            'Content-Type': 'plain/text;charset=utf-8'
          },
          body: id
        });
    }
}

function remove_task(id) {
    var response = fetch('http://127.0.0.1:443/back/remove-task', {
          method: 'POST',
          headers: {
            'Content-Type': 'plain/text;charset=utf-8'
          },
          body: id
        });
}

function add_task(name) {
    var n = document.getElementById('name').value
    if (n != null && n != "") {
        var response = fetch('http://127.0.0.1:443/back/add-task', {
          method: 'POST',
          headers: {
            'Content-Type': 'plain/text;charset=utf-8'
          },
          body: n
        });
    }
}