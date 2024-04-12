<template>
    <div id="productImage" class="carousel slide container " data-bs-ride="carousel">
        <!-- buttons indicators -->
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#productImage" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#productImage" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#productImage" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <!-- items -->
        <div class="carousel-inner">
            <!--  image item -->
            <div class="carousel-item active">
                <img src="../assets/1.jpg" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>First slide label</h5>
                    <p>Some representative placeholder content for the first slide.</p>
                </div>
            </div>

            <div class="carousel-item">
                <img src="../assets/2.png" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Second slide label</h5>
                    <p>Some representative placeholder content for the second slide.</p>
                </div>
            </div>

            <div class="carousel-item">
                <img src="../assets/1.jpg" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Third slide label</h5>
                    <p>Some representative placeholder content for the third slide.</p>
                </div>
            </div>
        </div>

        <!-- Next & previous -->
        <button class="carousel-control-prev" type="button" data-bs-target="#productImage" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#productImage" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</template>

<script>
export default {
    name: 'SliderComponent',
    data() {
        return {
            currentSlide: 0
        }
    },
    computed: {
        // slides() {
        //     return this.slider.slides;
        // },
        // currentSlideImage() {
        //     return this.slides[this.currentSlide].image;
        // }
    }
}
</script>

<style>
    #productImage{
        height: 400px;
        width: 100%;

    }
    #productImage img{
        height: 400px;
    }
    #productImage .carousel-item{
        height: 400px;
    }
    #productImage .carousel-item img{
        height: 400px;
    }
    #productImage .carousel-item img{
        object-fit: cover;
    }
    .carousel-item{
        height: 400px;
    }
    .carousel-control-prev-icon, .carousel-control-next-icon {
        height: 50px;
        width: 50px;
        outline: black;
        background-color: rgba(0, 0, 0);
        background-size: 100%, 100%;
        border-radius: 50%;
        border: 1px solid black;
    }
    
    .carousel-indicators [data-bs-target]{
        background-color: black;
    }
    #productImage .carousel-indicators button{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: black;
        opacity: 1;
    }
    #productImage .carousel-indicators .active{
        background-color: white;
    }
    
</style>