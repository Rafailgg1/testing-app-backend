async function deleteTodo(id) {
    const response = await fetch(`/todos/${id}/`, {
          method: 'delete',
          headers: {
              'Content-Type': 'application/json'
      },
      // body: JSON.stringify({
      //     'id': id
    });
    
    const data = await response.json();
  
  //   location.reload();
  if (response.ok) {
    element.remove();
  }
  }
  
  
  
  
      // const
  document.querySelectorAll('.todo-list')
  // .addEventListener('submit', function (event) {
  function deleteFormListener(event) {
      
  
   const form = event.target;
   console.log(form);
  
   if(form.classList.contains('delete-todo-form')) {
      event.preventDefault();
  
      const todoElement = form.closest('.todo'); 
      
      deleteTodo(todoElement.dataset.id);
      }
    }
  
  const todoList = document.querySelector('.todo-list')
  todoList.addEventListener('submit', deleteFormListener);
  
  
  //   }).then(function (response) {
  //     return response.json();
  //   }).then(function (data) {
  //     location.reload();
  //   })
  // }
    
    document.addEventListener('DOMContentLoaded', function () {
        const dropdowns = document.querySelectorAll('.dropdown');

        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('click', function () {
                this.querySelector('.dropdown-content').classList.toggle('show');
            });
        });

       
        window.addEventListener('click', function (e) {
            if (!e.target.matches('.dropdown')) {
                const dropdownContents = document.querySelectorAll('.dropdown-content');
                dropdownContents.forEach(content => {
                    content.classList.remove('show');
                });
            }
        });
    });
