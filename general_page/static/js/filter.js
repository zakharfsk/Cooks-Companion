let filetBtn = document.querySelectorAll('.filter-btn'),
    filter = document.querySelector('.filter');


    filetBtn.forEach(element => {
        element.onclick = () =>{
            if (filter.classList.contains('filter-active')) {
                filter.classList.remove('filter-active');
            } else {
                filter.classList.add('filter-active');
            }
        }
    });
