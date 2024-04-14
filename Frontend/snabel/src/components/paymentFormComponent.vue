<template>
    <main class="border border-2  border-danger d-flex align-items-center justify-content-center">
        <div class="border border-2  border-primary w-50">
            <div class=" d-flex flex-column justify-content-center align-items-center mx-5 w-75">

                <div class="d-flex ">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZYdiS6o83xt08rKMnams6WzHDiETtxkYcTg&s">
                    <h4 class="py-5">You're supporting TOGETHXR We Can Fund: Bras For Girls Your donation will benefit Bras for Girls</h4>
                </div>

                <div >
                <form class="row g-3 needs-validation"  novalidate>
                    <div>
                        <label for="" class="col-form-label">Enter your donation</label>
                        <div class="input-group mb-3">
                            <span class="input-group-text">$</span>
                            <span class="input-group-text">USD</span>
                            <input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
                            <span class="input-group-text">0.00</span>
                        </div>
                        <div>
                            <h4>Tip GoFundMe services</h4>
                            <h6>GoFundMe has a 0% platform fee for organizers. GoFundMe will continue offering its services thanks to donors who will leave an optional amount here:</h6>
                            <input type="range"  default value="10.25">
                        </div>
                        <label for="" class="col-form-label">Payment Method</label>
                        <div>
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                            <label class="form-check-label" for="flexRadioDefault1">PayPal</label>
                        </div>
                    </div>
                    <div  class=" paypal border border-2 border-info" >
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
                    <div>
                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
                        <label class="form-check-label" for="flexRadioDefault2">Credit</label>
                    </div>

                    <div class=" credit border border-2 border-info"  >
                        
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
                        <div>
                            <input class="form-check-input" type="checkbox" value="" >
                            <label class="form-check-label" for="invalidCheck">Save card for future donations</label>
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
                        <input type="text" class="form-control" placeholder="Your donation">
                        <input type="text" class="form-control" placeholder="GoFundMe tip">
                        <input type="text" class="form-control" placeholder="Total due today">
                    </div>
                    
                    <div class="col-12">
                        <button class="btn btn-primary " type="submit">Donate Now</button>
                    </div>
                    <div>
                        <h5 class="my-3">
                            By choosing the payment method above, you agree to the GoFundMe Terms of Service and acknowledge the <br> Privacy Notice.
                            Learn more about pricing and fees.
                        </h5>
                        <h6 class="my-5">
                            Certified Charity donations are made to PayPal Giving Fund, <br> minus transaction fees , and granted within 15-45 days, <br>
                            subject to its terms. In the unlikely event that there <br>
                            is a problem funding your chosen charity, PayPal Giving <br>
                            Fund will (whenever possible) ask you to recommend another,<br>
                            and grant the funds to a similar charity if you don’t respond.<br>
                            Your donation is typically tax deductible in the US.
                        </h6>
                    </div>
                </form>

                </div>
            </div>
        </div>
    </main>
</template>

<script>
export default {
    data:()=>({
        medhat:''
    }),
    methods:{
        // dd : function(){
        //     this.medhat=true
        // },

    }

}
</script>

<style scoped>

</style>