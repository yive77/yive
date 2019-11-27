<template>
    <form v-on:submit.prevent="onSubmit" class="ui form main-form">
        <div class="form-inner">
            <div class="form-error">{{ form_error }} </div>
            <div class="field">
                <label>First Name</label>
                <input v-model="firstName" type="text" name="first_name" placeholder="First Name" required>
            </div>
            <div class="field">
                <label>Last Name</label>
                <input v-model="lastName" type="text" name="last_name" placeholder="Last Name" required>
            </div>
            <div class="field">
                <label for="email">Email</label>
                <input v-model="email" id="email" type="text" placeholder="Email" required>
            </div>
            <div class="field">
                <label for="password">Password</label>
                <input v-model="password" id="password" type="text" placeholder="Password" required>
            </div>
            <button @click="register" class="ui button login-btn" type="submit">Register</button>
        </div>
    </form>
    
</template>

<script>
    /* eslint-disable no-alert, no-console */
    import axios from 'axios';
    import qs from 'querystring';

    const registerApi = "http://localhost:8081/api/register";

    export default {
        name: "Register",

        components: {

        },

        data: function() {
            return {
                firstName: '',
                lastName: '',
                email: '',
                password:  '',
                form_error: ''
            }
        },

        methods: {
            register: function() {
                let form = {
                    first_name: this.firstName,
                    last_name: this.lastName,
                    email: this.email,
                    password: this.password
                };
                
                var form_valid = true;

                for (var key in form) {
                    if (form[key].trim().length === 0) {
                        form_valid = false;
                    }
                }
                if (form_valid) {
                    axios.post(registerApi, qs.stringify(form)).then(response => {
                        console.log(response)
                        if (response.data.error) {
                            this.form_error = response.data.message
                        } else if (response.data.success) {
                            console.log("registration success")
                            this.$router.push('/login');
                        }
                    }).catch(error => {
                        console.log(error);
                    })
                } else {
                    this.form_error = "All fields are required";
                }
            },
            onSubmit: function() {
                
            }
        }
    }
</script>

<style lang="scss" scoped>

    .form-error {
        color: $error-color;
    }
</style>
