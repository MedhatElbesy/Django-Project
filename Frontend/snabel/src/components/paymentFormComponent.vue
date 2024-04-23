<template>
    <main class="d-flex align-items-center justify-content-center firstcontainer ">
        <div class="col-lg-8 col-md-10 col-sm-12 secondcontainer my-5">
            <div class="d-flex flex-column justify-content-center align-items-center mx-5">
                <div class="box d-flex py-3">
                    <img :src="getImageUrl(project.picture)">
                    <p class="py-1 px-2">You're supporting <b>{{project.user_name}}</b> which has Project description <b>{{project.description}}</b></p>
                </div>
                    <form class="row g-3 needs-validation" novalidate >
                        <div class="col-12">
                            <label for="" class="col-form-label">Enter your donation</label>
                            <div class="input-group mb-3">
                                <span class="input-group-text">
                                    <select class="form-select" id="validationCustom04" v-model="selectedCurrency" required>
                                        <option selected disabled value="Currency">Currency</option>
                                        <option value="USD">USD</option>
                                        <option value="EUR">EUR</option>
                                    </select>
                                </span>
                                <input type="text" name="money" v-model="donationAmount" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
                            </div>
                            <div>
                                <h4>Tip GoFundMe services</h4>
                                <p>GoFundMe has a 0% platform fee for organizers. GoFundMe will continue offering its services thanks to donors who will leave an optional amount here:</p>
                                <div class="progress">
                                    <div class="progress-bar progress-bar-striped" role="progressbar" :style="{ width: (project.total_collected / project.total_target) * 100+ '%' }" :aria-valuenow="project.total_collected" aria-valuemin="0" aria-valuemax="project.total_target">{{ (project.total_collected / project.total_target) * 100 }}%</div>
                                </div>
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
                                    By choosing the payment method above, you agree to the GoFundMe <router-link to="/terms">Terms of Service</router-link> and acknowledge the <br>
                                    <router-link to="/privacy">Privacy Notice</router-link> Learn more about <router-link to="/privacy">pricing and fees.</router-link>
                                </p>
                                <p class="my-5">
                                    Certified Charity donations are made to PayPal Giving Fund, <br>
                                    minus transaction fees, and granted within 15-45 days, <br>
                                    subject to its <router-link to="/terms">Terms</router-link>. In the unlikely event <router-link to="/contactus">that there is a problem funding your chosen Post</router-link>, PayPal Giving <br>
                                    Fund will (whenever possible) ask you to recommend another, <br>
                                    and grant the funds to a similar charity if you don’t respond. <br>
                                    Your donation is typically tax deductible in the US.
                                </p>
                            </div>
                        </div>
                </form>
            </div>
          </div>
  </main>
</template>

<script>
// import { useProjectStore } from "../stores/project";
import { ref, watchEffect, inject } from "vue";

export default {
    data:() =>({
        selectedMethod: 'paypal' ,
        donationAmount: 0,
        selectedCurrency: "USD",
        project:{},
        conversionRates: {
          USD: 1,
          EUR: 1.18 
    },
    }),
    methods: {
        getImageUrl(image) {
          return `http://127.0.0.1:8000${image}`;
}
,
        submitForm() {
          const userData = sessionStorage.getItem('user');
        const token = JSON.parse(sessionStorage.getItem("user")).token;
          if (!userData || !token) {
              alert('You must log in first');
              return; 
          }
          const deadlineDate = new Date(this.project.deadline);
          if (deadlineDate <= new Date()) {
              alert('Timeout: The project deadline has passed.');
              return; 
          }
          const amountToSubmit = this.selectedCurrency === 'EUR' ? 
              this.donationAmount * this.conversionRates.EUR : this.donationAmount;
          if (amountToSubmit <= 0 || isNaN(amountToSubmit)) {
              alert('Please enter a positive donation amount.');
              return; 
          }
          const formData = {
              amount: amountToSubmit,
              currency: this.selectedCurrency,
              user:userData.user.id ,
              project: this.project.id, 
          };
          fetch('http://127.0.0.1:8000/payment/create/', {
              method: 'POST',
              headers: {
                    'Authorization': `Bearer ${token}`,
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(formData),   
          })
          .then(response => {
            if (!response.ok) {
                throw new Error('Payment failed');
            }
            return response.json();
          })
          .then(data => {
            alert('Payment done successfully.');
            console.log('Data sent successfully:', data);
          })
          .catch(error => {
            console.error('Error sending data:', error);
            alert('Payment failed. Please try again later.');
          });
        }
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
            const tip = parseFloat(this.tip);
            const donationAmount = parseFloat(this.donationAmount);
                return tip + donationAmount;
        },
    },
    async created() {
        try {
        const projectStore = inject("projectStore");
        const projectID = ref(null);
        const projectData = ref(null);
        watchEffect(() => {
            projectID.value = projectStore.projectID;
            projectData.value = projectStore.projectData;
        });
        this.project = projectData;
        } catch (e) {
        console.log("Error is", e);
        }
    },
};
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
        max-width: 600px;
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
    .container-fluid{
        padding: 0 !important;
    }
    
</style>
