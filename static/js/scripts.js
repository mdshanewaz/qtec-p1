document.getElementById('get_data').addEventListener('click', loadData);


function loadData() {

    let xhr = new XMLHttpRequest();

    xhr.open('GET', 'http://127.0.0.1:8000/search/', true)

    xhr.onload = function() {
        if (this.status === 200) {   

            let data = JSON.parse(this.responseText);
            let prod = data.products;
            let size = prod.length;

            console.log(prod);

            var category = document.getElementById('category').value;
            var brand = document.getElementById('brand').value;

            category = Number(category);
            brand = Number(brand);

            // console.log(typeof(prod[6].category_id))

            let filtered_prod = [];

            for(let j=0; j<size; j++) {
                if (category === 0) {
                    if (brand === 0) {
                        filtered_prod.push(prod[j]);
                    }
                    else if (prod[j].brand_id === brand) {
                        filtered_prod.push(prod[j]);
                    }
                }
                else if (prod[j].category_id === category) {
                    if (brand === 0) {
                        filtered_prod.push(prod[j]);
                    }
                    else if (prod[j].brand_id === brand) {
                        filtered_prod.push(prod[j]);
                    }
                };

            };


            size_of_filter = filtered_prod.length;

            let searchResultsHolder = document.getElementById('search-results-holder');
            searchResultsHolder.innerHTML = '';

            let searchResultscontainer = document.getElementById('search-results');
            searchResultscontainer.innerHTML = '';


            for(let i=0; i<size_of_filter; i++) { 

                imageUrl = "/media/" + filtered_prod[i].mainimage+"";

                 let productHTML = `
                <div class="col-md-6 col-sm-12 col-lg-3" id="search-results-container">
                    <figure class="card card-product">
                        <div class="img-wrap">
                            <img src="${imageUrl}" class="img img-fluid product_img" alt="" style="width: 100%; height: 300px;">
                        </div>
                        <figcaption class="info-wrap">
                            <h6 class="title"><a href="#" class="product_name">${filtered_prod[i].name}</a></h6>
                            <div class="action-wrap">
                                <div class="price-wrap h5">
                                    <span class="price-new">Price: &#2547; ${filtered_prod[i].price}</span>
                                    <br>
                                <span class="price-old">Old Price: &#2547; <strike id="price_old">${filtered_prod[i].old_price}</strike>
                                    </span>
                                </div>
                            </div>
                        </figcaption>
                    </figure>
                </div>
                `;
                searchResultsHolder.innerHTML += productHTML;
            };
        }
    }

    xhr.send();
}