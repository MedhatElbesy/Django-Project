<template>
    <main class=" d-flex align-items-center justify-content-center firstcontainer">
        <div class=" w-50 secondcontainer my-5">
            <div class="d-flex flex-column justify-content-center align-items-center mx-5 w-75">

                <div class=" box d-flex py-3">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZYdiS6o83xt08rKMnams6WzHDiETtxkYcTg&s">
                    <p class="py-1 px-2">You're supporting TOGETHXR We Can Fund: Bras For Girls Your donation will benefit Bras for Girls</p>
                </div>

                <div>
                    <form class="row g-3 needs-validation" novalidate>
                        <div>
                            <label for="" class="col-form-label ">Enter your donation</label>
                            <div class="input-group mb-3">
                                <span class="input-group-text">$</span>
                                <span class="input-group-text">USD</span>
                                <input type="text" v-model="donationAmount" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
                                <span class="input-group-text">0.00</span>
                            </div>
                            
                            <div>
                                <h4>Tip GoFundMe services</h4>
                                <p>GoFundMe has a 0% platform fee for organizers. GoFundMe will continue offering its services thanks to donors who will leave an optional amount here:</p>
                                <div class="progress">
                                    <div class="progress-bar" role="progressbar" :style="{width: donationPercentage +'%'}" aria-valuenow="donationPercentage" aria-valuemin="0" aria-valuemax="100">{{donationPercentage}} %</div>
                                </div>
                            </div>
                            <label for="" class="col-form-label">Payment Method</label>
                            <div>
                                <input class="form-check-input" type="radio" name="paymentMethod" id="paypalRadio" v-model="selectedMethod" value="paypal">
                                <label class="form-check-label" for="paypalRadio">PayPal</label>
                            </div>
                            <div>
                                <input class="form-check-input" type="radio" name="paymentMethod" id="creditRadio" v-model="selectedMethod" value="credit">
                                <label class="form-check-label" for="creditRadio">Credit</label>
                            </div>
                        </div>

                        <div v-if="selectedMethod === 'paypal'" class="paypal ">
                            <label for="validationCustom01" class="form-label" >First name</label>
                            <input type="text" class="form-control" id="validationCustom01" value="" required>
                            <div class="valid-feedback">Looks good!</div>

                            <label for="validationCustom02" class="form-label">Last name</label>
                            <input type="text" class="form-control" id="validationCustom02" value="" required>
                            <div class="valid-feedback">Looks good!</div>

                            <label for="validationCustomUsername" class="form-label">Email</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="inputGroupPrepend">@</span>
                                <input type="text" class="form-control" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
                                <div class="invalid-feedback">Please choose a username.</div>
                            </div>

                            <label for="validationCustom04" class="form-label">City</label>
                            <select class="form-select" id="validationCustom04" required>
                                <option selected disabled value="">City</option>
                                <option selected>Countary</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                            <div class="invalid-feedback">Please select a valid state.</div>
                            
                            <label for="validationCustom05" class="form-label">Postal Code</label>
                            <input type="number" class="form-control" id="validationCustom05" required>
                            <div class="invalid-feedback">Please provide a valid Postal Code.</div>
                        </div>

                        <div v-if="selectedMethod === 'credit'" class="credit ">
                            <label for="validationCustom01" class="form-label">First name</label>
                            <input type="text" class="form-control" id="validationCustom01" value="" required>
                            <div class="valid-feedback">Looks good!</div>

                            <label for="validationCustom02" class="form-label">Last name</label>
                            <input type="text" class="form-control" id="validationCustom02" value="" required>
                            <div class="valid-feedback">Looks good!</div>

                            <label for="validationCustomUsername" class="form-label">Email</label>
                            <div class="input-group has-validation">
                                <span class="input-group-text" id="inputGroupPrepend">@</span>
                                <input type="text" class="form-control" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
                                <div class="invalid-feedback">Please choose a username.</div>
                            </div>

                            <div class="my-3">
                                <input class="form-check-input" type="checkbox" value="" >
                                <label class="form-check-label" for="invalidCheck">Save card for future donations</label>
                            </div>
                            <div>
                                <label for="validationCustom05" class="form-label">Card Number</label>
                                <input type="number" class="form-control" id="validationCustom05" required>
                                <div class="invalid-feedback">Please provide a valid Card Number.</div>
                            </div>
                            <div class="d-flex justify-content-between">
                                <div>
                                    <label for="validationCustom05" >Date</label>
                                    <input type="date" class="form-control" id="validationCustom05" required>
                                    <div class="invalid-feedback">Please provide a Date.</div>
                                </div>
                                <div>
                                    <label for="ccn" >CVV</label>
                                    <input type="tel" inputmode="numeric" autocomplete="cc-number" maxlength="19" class="form-control" pattern="[0-9\s]{13,19}" id="cnn" placeholder="xxxx xxxx xxxx xxxx" required >
                                    <div class="invalid-feedback">Please provide a valid CVV.</div>
                                </div>
                            </div>

                            <label for="validationCustom04" class="form-label">City</label>
                            <select class="form-select" id="validationCustom04" required>
                                <option selected disabled value="">City</option>
                                <option selected>Countary</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                            </select>
                            <div class="invalid-feedback">Please select a valid state.</div>
                            
                            <label for="validationCustom05" class="form-label">Postal Code</label>
                            <input type="text" class="form-control" id="validationCustom05" required>
                            <div class="invalid-feedback">Please provide a valid Postal Code.</div>
                            <div class="py-3">
                                <input class="form-check-input" type="checkbox">
                                <label class="form-check-label" for="invalidCheck"> Save card for future donations</label>
                            </div>
                        </div>

                        <div class="my-5">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                <label class="form-check-label" for="flexCheckDefault">Don't display my name publicly on the fundraiser</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
                                <label class="form-check-label" for="flexCheckChecked">Get occasional marketing updates from GoFundMe. You may unsubscribe at any time.</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
                                <label class="form-check-label" for="flexCheckChecked">I'm happy to provide this charity my name and email, so they can notify me about other ways that I can help. I understand that I can unsubscribe at any time by contacting the charity.</label>
                            </div>
                        </div>
                        <div>
                            <label  class="form-label ">Your donation</label>
                            <input type="text" disabled class="form-control" placeholder="Your donation" :value="donationAmount">
                            <label  class="form-label ">Tip</label>
                            <input type="text" disabled class="form-control" placeholder="GoFundMe tip" :value="tip">
                            <label  class="form-label ">Total</label>
                            <input type="text" disabled class="form-control" placeholder="Total due today" :value="total">
                        </div>

                        <div class="col-12">
                            <button class="btn btn-primary " type="submit">Donate Now</button>
                        </div>
                        <div>
                            <p class="my-3">
                                By choosing the payment method above, you agree to the GoFundMe Terms of Service and acknowledge the <br> Privacy Notice.
                                Learn more about pricing and fees.
                            </p>
                            <p class="my-5">
                                Certified Charity donations are made to PayPal Giving Fund, <br> minus transaction fees , and granted within 15-45 days, <br>
                                subject to its terms. In the unlikely event that there <br>
                                is a problem funding your chosen charity, PayPal Giving <br>
                                Fund will (whenever possible) ask you to recommend another,<br>
                                and grant the funds to a similar charity if you don’t respond.<br>
                                Your donation is typically tax deductible in the US.
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
// Example starter JavaScript for disabling form submissions if there are invalid fields
    (function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
        })
    })()
export default {
    data:() =>({
        selectedMethod: 'paypal' ,
        donationAmount: 0
    }),
    methods:{
        
    },
    computed:{
        donationPercentage(){
            return (parseFloat(this.donationAmount) / 100) * 10 ;
        },
        tip(){
            let tiip = this.donationPercentage;
            return tiip += tiip *.2
        },
        total() {
            const tip = parseFloat(this.tip);
            const donationAmount = parseFloat(this.donationAmount);
                return tip + donationAmount;
        }

    }
}

</script>

<style scoped>
    img{
        border-radius: 10px;
        height: 100px;
    }
    label{
        font-weight:bold;
    }
    .firstcontainer{
        background-color: #4e6c881e;
    }
    .secondcontainer{

        border-radius: 50px;
        background-color: white;
    }

</style>








