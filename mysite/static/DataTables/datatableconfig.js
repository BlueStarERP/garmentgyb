console.log('config success');


new DataTable('#example');


      
new DataTable('#columnsearch', {
    
    initComplete: function () {
        this.api()
            .columns()
            .every(function () {
                let column = this;
                let title = column.header().textContent;
 
                // Create input element
                let input = document.createElement('input');
                input.placeholder = title;
                column.header().replaceChildren(input);
 
                // Event listener for user input
                input.addEventListener('keyup', () => {
                    if (column.search() !== this.value) {
                        column.search(input.value).draw();
                    }
                });
            });
    },
    layout: {
        topStart: {
            buttons: ['excel', 'pdf', 'print']
            
            
            
        },
    },
    paging: false
});

