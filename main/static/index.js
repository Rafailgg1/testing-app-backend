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
// Обновляем отображение текущего URL
function updateUrlDisplay() {
    const urlDisplay = document.getElementById('url-display');
    urlDisplay.textContent = window.location.pathname;
}

// Вызываем при загрузке страницы
updateUrlDisplay();

// Вызываем при изменении URL
window.addEventListener('popstate', updateUrlDisplay);
 
document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');

    // Обработчик для раскрытия/закрытия выпадающего списка
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', function (e) {
            e.stopPropagation(); // Останавливаем всплытие события
            this.querySelector('.dropdown-content').classList.toggle('show');
        });
    });

    // Закрываем выпадающие списки при клике вне их области
    window.addEventListener('click', function () {
        dropdowns.forEach(dropdown => {
            dropdown.querySelector('.dropdown-content').classList.remove('show');
        });
    });

    // Добавляем класс 'active' к текущему пункту меню
    const currentUrl = window.location.pathname; // Получаем текущий URL
    const navLinks = document.querySelectorAll('.nav__link, .dropdown-content a');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });

    // Обработчик для изменения URL без перезагрузки страницы
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault(); // Отменяем стандартное поведение ссылки
            const url = this.getAttribute('href');

            // Изменяем URL без перезагрузки страницы
            history.pushState(null, null, url);

            // Добавляем класс 'active' к текущему пункту меню
            navLinks.forEach(link => link.classList.remove('active'));
            this.classList.add('active');

            // Здесь можно добавить логику для загрузки контента (например, через AJAX)
            console.log(`Переход на ${url}`);
        });
    });
});