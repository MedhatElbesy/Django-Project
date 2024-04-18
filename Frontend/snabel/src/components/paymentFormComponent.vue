<template>
    <main class="d-flex align-items-center justify-content-center firstcontainer">
        <div class=" w-50 container secondcontainer my-5">
            <div class="row justify-content-center">
                <div class="col-lg-8 col-md-10 col-sm-12">
                    <div class="d-flex flex-column justify-content-center align-items-center mx-5">
                        <div class="box d-flex py-3">
                            <img src="https://media.istockphoto.com/id/1283030328/photo/silhouette-of-businessman-holding-target-board-on-the-top-of-mountain-with-over-blue-sky-and.jpg?s=612x612&w=0&k=20&c=2ZifINbmOZq9dWW8iviW1k275x2zDy8w5_TBuLB5Sso=">
                            <p class="py-1 px-2">You're supporting <b>{{project.user_name}}</b> which has Project description <b>{{project.description}}</b></p>
                        </div>
                            <form class="row g-3 needs-validation" novalidate >
                                <div class="col-12">
                                    <label for="" class="col-form-label">Enter your donation</label>
                                    <div class="input-group mb-3">
                                        <span class="input-group-text">
                                            <select class="form-select" id="validationCustom04" v-model="currency" required>
                                                <option selected disabled :value="currency">Currency</option>
                                                <option value="USD">USD</option>
                                                <option value="EUR">EUR</option>
                                            </select>
                                        </span>
                                        <input type="text" name="money" v-model="donationAmount" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
                                        <span class="input-group-text">0.00</span>
                                    </div>
                                    <div>
                                        <h4>Tip GoFundMe services</h4>
                                        <p>GoFundMe has a 0% platform fee for organizers. GoFundMe will continue offering its services thanks to donors who will leave an optional amount here:</p>
                                        <div class="progress">
                                            <div class="progress-bar" role="progressbar" :style="{ width: tip/100 + '%' }" :aria-valuenow="tip" aria-valuemin="0" aria-valuemax="100">{{ tip }}%</div>
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
                                <div v-if="selectedMethod === 'paypal'" class="paypal col-12">
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

                                    <label for="validationCustom04" class="form-label">City</label>
                                    <select class="form-select" id="validationCustom04" required>
                                        <option selected disabled value="">City</option>
                                        <option selected>Country</option>
                                        <option value="1">One</option>
                                        <option value="2">Two</option>
                                        <option value="3">Three</option>
                                    </select>
                                    <div class="invalid-feedback">Please select a valid state.</div>
                                                                
                                    <label for="validationCustom05" class="form-label">Postal Code</label>
                                    <input type="number" class="form-control" id="validationCustom05" required>
                                    <div class="invalid-feedback">Please provide a valid Postal Code.</div>
                                </div>
                                <div v-if="selectedMethod === 'credit'" class="credit col-12">
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

                                    <div class="d-flex justify-content-between flex-column">
                                        <label for="ccn">Credit Card Number</label>
                                        <input id="ccn" type="tel" inputmode="numeric" class="form-control my-2" pattern="[0-9\s]{13,19}" 
                                        autocomplete="cc-number" maxlength="19" placeholder="xxxx xxxx xxxx xxxx" required>
                                        <div class="invalid-feedback">Please provide a valid Card Number.</div>
                                    </div>
                                    
                                    <div class="d-flex justify-content-between flex-column flex-md-row"> 
                                        <div class="mb-3 mb-md-0"> 
                                            <label for="validationCustom05">Date</label>
                                            <input type="date" class="form-control" id="validationCustom05" required>
                                            <div class="invalid-feedback">Please provide a Date.</div>
                                        </div>
                                        <div class="mx-2 mb-3 mb-md-0"> 
                                            <label for="cvv" class="form-label  ">CVV</label>
                                            <input type="text" id="cvv" class="form-control" placeholder="xxx" v-model="cvv" required pattern="[0-9]{3,4}">
                                            <div class="invalid-feedback"> Please provide a valid CVV.</div>
                                        </div>
                                    </div>
                                    <label for="validationCustom04" class="form-label">City</label>
                                    <select class="form-select" id="validationCustom04" required>
                                        <option selected disabled value="">City</option>
                                        <option selected>Country</option>
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
                                <div class="col-12">
                                    <div>
                                        <label class="form-label">Your donation</label>
                                        <input type="text" disabled class="form-control" placeholder="Your donation" :value="donationAmount">
                                        <label class="form-label">Tip</label>
                                        <input type="text" disabled class="form-control" placeholder="GoFundMe tip" :value="tip">
                                        <label class="form-label">Total</label>
                                        <input type="text" disabled class="form-control" placeholder="Total due today" :value="total">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <button class="btn btn-primary" type="submit" @click.prevent="submitForm">Donate Now</button>
                                </div>
                                <div class="col-12">
                                    <div>
                                        <p class="my-3">
                                            By choosing the payment method above, you agree to the GoFundMe <a href="#">Terms of Service</a> and acknowledge the <br>
                                            <a href="#">Privacy Notice.</a> Learn more about <a href="#">pricing and fees.</a>
                                        </p>
                                        <p class="my-5">
                                            Certified Charity donations are made to PayPal Giving Fund, <br>
                                            <a href="#">minus transaction fees</a>, and granted within <a href="#">15-45 days</a>, <br>
                                            subject to its <a href="#">terms</a>. In the unlikely event <a href="#">that there is a problem funding your chosen charity</a>, PayPal Giving <br>
                                            Fund will (whenever possible) ask you to recommend another, <br>
                                            and grant the funds to a similar charity if you don’t respond. <br>
                                            Your donation is typically tax deductible in the US.
                                        </p>
                                    </div>
                                </div>
                            </form>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>



<script>
// import axios from 'axios';
import { useProjectStore } from "../stores/project";
export default {
    data:() =>({
        selectedMethod: 'paypal' ,
        donationAmount: 0,
        currency: "USD",
        project:{},
    }),
    methods: {
        collected(){
            if(this.project.total_target < (this.project.total_target+this.donationAmount)){
                this.donationAmount=(this.project.total_target-this.project.total_target)
            }else{
                return this.donationAmount;
            }
        },
        submitForm() {
            if(this.project.deadline > Date.now()){
                const formData = {
                    amount: this.total,
                    currency: this.currency,
                    user:this.project.user,
                    project: 2,
                };
                fetch('http://127.0.0.1:8000/payment/create/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData),
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    
                    console.log('Data sent successfully:', data);
                    // console.log(data);
                    // console.log("medhat");
                })
                
                .catch(error => {
                    console.error('Error sending data:', error);
                });
            }else
                alert('Timeout: The project deadline has passed.');
        },
}
    ,
    computed:{
        donationPercentage(){
            return (parseFloat(this.donationAmount)) / 100 ;
        },
        tip(){
            return  (parseInt(this.donationPercentage));
        },
        total() {
            this.collected();
            const tip = parseFloat(this.tip);
            const donationAmount = parseFloat(this.donationAmount);
                return tip + donationAmount;
        },
    },
    async created(){
            try{
                let myproject =  useProjectStore();
                myproject.projectID = 1;
                await myproject.fetchProjectData();
                this.project =  myproject.projectData;
                console.log(this.project);
                console.log('uuuuuuuuuuuuuuuuuuu');
            }catch(e){
                console.log("Error is",e);
            }
        },
    
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
    .paypal input[type="text"],
    .paypal select,
    .paypal input[type="date"] {
        border-radius: 10px; 
    }
    .credit input[type="text"],
    .credit select,
    .credit input[type="date"] {
        border-radius: 5px; 
    }
    
</style>








