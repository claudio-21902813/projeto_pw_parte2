function showSection(section) {
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });
         document.querySelector(`#${section}`).style.display = 'block';
    if(section != "apple" && section != "windows" && section != "linux")
    {
     document.querySelector(`#${section}`).style.display = 'block';
         fetch(`sections/${section}`)
    .then(response => response.text())
    .then(text =>
     document.querySelector(`#${section}`).innerHTML = text);
    }
}

document.addEventListener('DOMContentLoaded', function() {

     // envia pedido GET ao URL
        fetch('getNews')
        // converte a resposta em formato json
        .then(response => response.json())
        .then(data => {
            data.Apple.forEach(add_post_apple);
            data.Windows.forEach(add_post_windows);
            data.Linux.forEach(add_post_linux);
        })
        // Apanha erros e mostra-os na consola
        .catch(error => {
            console.log('Error:', error);
        });

       function add_post_apple(contents) {
                // create a List
                const post = document.createElement('ul');
                post.className = 'post';

                const a = document.createElement('a');
                a.href  = "www.google.pt";


                const h1 = document.createElement('h1');
                h1.innerHTML = contents['titulo'];

                const p = document.createElement('p');
                p.innerHTML = "Autor: " + contents['autor'] +  "  Data: " + contents['data'];

                const image = document.createElement('img');
                image.src = contents['imagem'];
                image.style.width  = "50%";
                image.style.height  = "50%";

                a.append(h1);
                a.append(p);
                a.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#apple').append(post);
            };

                   function add_post_windows(contents) {
                // create a List
                const post = document.createElement('ul');
                post.className = 'post';

                const a = document.createElement('a');
                a.href  = "www.google.pt";


                const h1 = document.createElement('h1');
                h1.innerHTML = contents['titulo'];

                const p = document.createElement('p');
                p.innerHTML = "Autor: " + contents['autor'] +  "  Data: " + contents['data'];

                const image = document.createElement('img');
                image.src = contents['imagem'];
                image.style.width  = "50%";
                image.style.height  = "50%";

                a.append(h1);
                a.append(p);
                a.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#windows').append(post);
            };

                   function add_post_linux(contents) {
                // create a List
                const post = document.createElement('ul');
                post.className = 'post';

                const a = document.createElement('a');
                a.href  = "www.google.pt";


                const h1 = document.createElement('h1');
                h1.innerHTML = contents['titulo'];

                const p = document.createElement('p');
                p.innerHTML = "Autor: " + contents['autor'] +  "  Data: " + contents['data'];

                const image = document.createElement('img');
                image.src = contents['imagem'];
                image.style.width  = "50%";
                image.style.height  = "50%";

                a.append(h1);
                a.append(p);
                a.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#linux').append(post);
            };

    document.querySelectorAll('a').forEach(button => {
    button.onclick = function() {
        const section = this.dataset.section;
        history.pushState({section:section},"",`section${section}`);
        showSection(this.dataset.section);
        };
    });
});