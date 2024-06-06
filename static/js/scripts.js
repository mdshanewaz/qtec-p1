document.getElementById('get_data').addEventListener('click', loadData);

function loadData() {

    let xhr = new XMLHttpRequest();

    xhr.open('GET', 'http://127.0.0.1:8000/search/', true)

    xhr.onload = function() {
        if (this.status === 200) {   

            let data = JSON.parse(this.responseText);
            let prod = data.products;
            let size = prod.length;

            console.log(prod)

            let img = document.querySelector('.product_img');
            let product_name= document.querySelector('.product_name');
            let price_new = document.querySelector('.price-new');
            let price_old = document.querySelector('.price_old');


            for(let i=0; i<size; i++) { 

                // product_name.innerHTML = 
                // price_new.innerHTML = 
                // price_old.innerHTML = 
                // img.src = 

                <figure class="card card-product">
                    <div class="img-wrap">
                        <img src="/media/ + prod[i].mainimage" class="img img-fluid product_img" alt="" style="width: 100%; height: 300px;">
                    </div>
                    <figcaption class="info-wrap">
                        <h6 class="title"><a href="#" class="product_name">prod[i].name;</a></h6>
                         <div class="action-wrap">
                            <div class="price-wrap h5">
                                <span class="price-new">Price: &#2547; prod[i].price</span>
                                <br>
                               <span class="price-old">Old Price: &#2547; <strike id="price_old">prod[i].old_price;</strike>
                                </span>
                            </div>
                        </div>
                    </figcaption>
                </figure>

            };
        }
    }

    xhr.send();
}