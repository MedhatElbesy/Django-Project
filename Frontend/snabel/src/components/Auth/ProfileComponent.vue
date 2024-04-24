<template>
    <div class="search">
      <nav class="row g-0">
        <navbar />
        <navbarResp />
      </nav>
      <section class="row g-0 justify-content-center align-items-center text-center mb-3">
      <div class="content mt-5">
        <h2 class="mb-4 color">Account Settings</h2>
      </div>
    </section>

    <section class="row g-0 mb-5 p-2 justify-content-center align-items-center">
      <div class="col-lg-6 col-xl-6">
        <div class="card m-2 border-0 text-black h-75 bg-transparent">
          <div class="card-body p-4">
            <div class="row justify-content-center align-items-center">
              <!-- Start Messages -->
              <div v-if="successMessages" class="alert alert-success alert-dismissible fade show  p-2" role="alert">
                <strong class="mb-0">{{ successMessages }}</strong>
                <button aria-label="Close" class="btn-close" data-bs-dismiss="alert" style="height: auto;"
                        type="button"></button>
              </div>

              <div v-for="(messages, field) in errorMessages" :key="field"
                   class="alert alert-danger alert-dismissible fade show  p-2" role="alert">
                <ul class="mb-0">
                  <li v-for="message in messages" :key="message" class="p-0 bullet-list">{{ message }}</li>
                </ul>
                <button aria-label="Close" class="btn-close" data-bs-dismiss="alert" style="height: auto;"
                        type="button"></button>
              </div>
              <!-- End Of Messages -->
              <!-- Form Here -->
              <form class="mx-1 mx-md-4 m-auto" enctype="multipart/form-data" @submit.prevent="authenticationStore.updateProfile">
                <div class="d-flex justify-content-center mb-5">
                  <div class="me-4">
                    <div id="image_preview"
                         class="bg-light border position-relative border-1 d-inline-block text-center rounded rounded-circle position-relative overflow-hidden"
                         @click="triggerFileInput">
                      <img :src="authenticationStore.getProfileImageUrl(authenticationStore.user.profile_image)" alt="Current Image"
                           class="rounded rounded-circle"
                           height="100">
                      <i class="fas fa-camera position-absolute" style="bottom: 15px; right: 8px;"></i>
                    </div>
                    <input id="image_input" accept="image/*" name="profile_image" style="display: none;" type="file"
                           @change="handleFileChange">
                  </div>
                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input v-model="authenticationStore.user.first_name" aria-describedby="first_name"
                             aria-label="first_name" autofocus
                             class="form-control border-0 border-bottom shadow" name="first_name"
                             placeholder="enter your first name" type="text">
                      <i class="fa-solid fa-user icon position-absolute"></i>
                      <label for="first_name">First Name</label></div>
                  </div>
                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input v-model="authenticationStore.user.last_name" aria-describedby="last_name"
                             aria-label="last_name" autofocus
                             class="form-control border-0 border-bottom shadow" name="last_name"
                             placeholder="enter your last name" type="text">
                      <i class="fa-solid fa-user icon position-absolute"></i>
                      <label for="last_name">Last Name</label></div>
                  </div>
                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input :value="authenticationStore.user.email" aria-describedby="email"
                             aria-label="email" autofocus class="form-control border-0 border-bottom shadow"
                             name="email" placeholder="enter your email"
                             readonly type="text">
                      <i class="fa-solid fa-envelope icon position-absolute"></i>
                      <label for="email">Email</label></div>
                  </div>
                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input v-model="authenticationStore.user.mobile_phone" aria-describedby="mobile_phone" aria-label="mobile_phone"
                             class="form-control border-0 border-bottom shadow" name="mobile_phone"
                             placeholder="enter your mobile phone"
                             type="text">
                      <i class="fa-solid fa-mobile icon position-absolute"></i>
                      <label for="mobile_phone">Mobile Phone</label>
                    </div>
                  </div>
                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input v-model="authenticationStore.user.birthdate" aria-describedby="birthdate" aria-label="birthdate"
                             class="form-control border-0 border-bottom shadow" name="birthdate"
                             placeholder="enter your birthdate"
                             type="date">
                      <i class="fa-solid fa-calendar-days icon position-absolute"></i>
                      <label for="birthdate">Birthdate</label>
                    </div>
                  </div>

                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input v-model="authenticationStore.user.facebook_profile" aria-describedby="facebook_profile"
                             aria-label="facebook_profile"
                             class="form-control border-0 border-bottom shadow" name="facebook_profile"
                             placeholder="enter your facebook url"
                             type="text">
                      <i class="fa-solid fa-link icon position-absolute"></i>
                      <label for="facebook_profile">Facebook Profile URL</label>
                    </div>
                  </div>
                </div>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-5">
                  <div class="col">
                    <div class="form-floating position-relative">
                      <input v-model="authenticationStore.user.country" aria-describedby="country"
                             aria-label="country"
                             class="form-control border-0 border-bottom shadow" name="country"
                             placeholder="enter your country name"
                             type="text">
                      <i class="fa-solid fa-globe icon position-absolute"></i>
                      <label for="country">Country</label>
                    </div>
                  </div>
                </div>

                <div class="row justify-content-between align-items-center mb-5 mx-2">
                  <button class="btn btn-outline-secondary shadow rounded-pill p-2" type="submit">
                    Save Your Profile
                  </button>
                </div>
              </form>

              <!-- <hr>
              <div class="row m-2">
                <p class="text-danger">Deleting your account will remove all of your activity and campaigns, and you will no longer be
                  able to sign in with this account.</p>
                <button class="btn btn-lg rounded auth-button btn-outline-danger" type="submit">
                  Delete Account
                </button>
              </div> -->
            </div>
          </div>
        </div>
      </div>
    </section>
    <footer class="row g-0 bg-light">
      <footerComponent/>
    </footer>
  </div>
</template>

<script>
import {useAuthenticationStore} from "../../stores/auth";
import navbar from "@/components/navComponent.vue";
import navbarResp from "@/components/navRespComponent.vue";
import footerComponent from "@/components/footerComponent.vue";

export default {
  name: "RegisterComponent",
  components: {footerComponent, navbar, navbarResp},
  data: () => ({
    authenticationStore: useAuthenticationStore(),
    password1Visible: false,
    password2Visible: false,
    errorMessages: {},
    successMessages: '',
  }),

  mounted() {
    var userDataJSON = sessionStorage.getItem('user');

    var userDataWithExpiration = JSON.parse(userDataJSON);

    if (userDataWithExpiration && userDataWithExpiration.expiration > new Date().getTime()) {
      this.authenticationStore.user = userDataWithExpiration.user;
    } else {
      sessionStorage.removeItem('user');
      return null;
    }
  },

  methods: {
    togglePassword1Visibility() {
      this.password1Visible = !this.password1Visible;
      const passwordInput = document.querySelector('input[name="password1"]');
      if (passwordInput) {
        passwordInput.type = this.password1Visible ? 'text' : 'password';
      }
    },
    togglePassword2Visibility() {
      this.password2Visible = !this.password2Visible;
      const passwordInput = document.querySelector('input[name="password2"]');
      if (passwordInput) {
        passwordInput.type = this.password2Visible ? 'text' : 'password';
      }
    },
    triggerFileInput() {
      const fileInput = document.getElementById('image_input');
      fileInput.click(); // Simulate click on file input
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.authenticationStore.user.profile_image = file;
        const reader = new FileReader();
        reader.onload = () => {
          const output = document.getElementById('image_preview');
          output.innerHTML = `<img src="${reader.result}" alt="New Image" height="100">`;
        };
        reader.readAsDataURL(file);
      }
    }
  },
}
</script>


<style scoped>
.bullet-list {
  list-style-type: disc;
  margin-left: 20px;
}

.bullet-list li {
  margin-left: 10px;
}

.welcome {
  padding-top: 28px;
}

h3 {
  margin-bottom: 24px;
}

.ayat {
  text-align: center;
  direction: rtl;
  padding-bottom: 40px;
  font-weight: bold;
  color: var(--mainTextColor);
  letter-spacing: 2px;
  word-spacing: 3px;
  font-family: 'Reem Kufi', sans-serif;
}

em {
  font-size: 12px;
}

.login {
  border-top-left-radius: 52px;
  background-color: #FFF;
}

.signup {
  text-align: right;
}

.submit {
  position: fixed;
  right: 0;
  bottom: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-end;
  background-color: #FFF;
  padding: 25px;
  border-top: 1px solid #e2e2e2;
}

form input {
  color: var(--mainColor);
}

form input:focus {
  caret-color: var(--mainColor);
  color: var(--mainTextColor);
}

form label {
  color: var(--mainColor);
}

.icon {
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: var(--mainColor)
}

.social {
  padding-bottom: 150px;
}

.social p::before {
  content: "";
  position: absolute;
  height: 1px;
  width: 40%;
  top: 50%;
  left: 3%;
  transform: translateY(50%);
  border: 1px solid #8f8f8f48;
}

.social p::after {
  content: "";
  position: absolute;
  height: 1px;
  width: 40%;
  top: 50%;
  right: 3%;
  transform: translateY(50%);
  border: 1px solid #8f8f8f48;
}

.social-platforms a {
  color: #FFF;
  border-radius: 8px;
  display: inline-block;
}

.social-platforms i {
  padding: 12px;
  width: 40px;
}

.social-platforms span {
  padding: 12px;
  width: 200px;
  display: inline-block;
  border-radius: 8px;
}

.social-platforms li:first-child a {
  background-color: #C53329;
}

.social-platforms li:first-child span {
  background-color: #F44235;
  border-left: 1px solid #e76464;
}

.social-platforms li:last-child a {
  background-color: #3A5998;
}

.social-platforms li:last-child span {
  background-color: #243B68;
  border-left: 1px solid #4666a7;
}

@media screen and (max-width: 992px) {
  .login {
    border-top-right-radius: 52px;
  }
}

@media screen and (max-width: 576px) {
  form {
    width: 100% !important;
    padding-right: 16px;
    padding-left: 16px;
  }

  .submit {
    position: static;
    justify-content: center;
  }

  .social {
    padding-bottom: 0;
  }
}
</style>