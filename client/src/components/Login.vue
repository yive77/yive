
<template>
    <form v-on:submit.prevent="onSubmit" class="ui form main-form">
        <div class="form-inner">
            <div class="form-error">{{ form_error }}</div>
            <div class="field">
                <label for="login-email">Email</label>
                <input v-model="email" id="login-email" type="email" name="email" placeholder="Email">
            </div>
            <div class="field">
                <label for="password">Password</label>
                <input v-model="password" id="password" type="password" name="Password" placeholder="Password">
            </div>
            
            <button @click="login" class="ui button login-btn" type="submit">Login</button>
        </div>
    </form>
</template>

<script>
    /* eslint-disable no-alert, no-console */

    import qs from 'querystring';
    import axios from 'axios';
    const login_url = "http://localhost:8081/api/login";

    export default {
        name: "Login",
        data: () => {
            return { 
                email: '',
                password: '',
                form_error: ''
            }
        },
        methods: {
            login: function() {
                let form = {
                    email: this.email.trim(),
                    password: this.password.trim(),
                    
                }

                if (form.email.length > 0 && form.password.length > 0) {
                    axios.post(login_url, qs.stringify(form)).then(response => {
                        if (response.data.error) {
                            this.form_error = response.data.message;
                        } else {
                            alert("login successful");
                        }
                    }).catch(error => {
                        console.log(error);
                    })
                } else {
                    this.form_error = "All fields are required."
                }
            },
            onSubmit: () => {}
        },
        computed: {
        }
    }
</script>

<style lang="scss">
    .main-form {
        @extend .main-form;
    }
</style>
