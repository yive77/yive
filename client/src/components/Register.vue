<template>
    <form v-on:submit.prevent="onSubmit" class="ui form main-form">
        <div class="form-inner">
            <div class="field">
                <label>First Name</label>
                <input v-model="firstName" type="text" name="first_name" placeholder="First Name">
            </div>
            <div class="field">
                <label>Last Name</label>
                <input v-model="lastName" type="text" name="last_name" placeholder="Last Name">
            </div>
            <div class="field">
                <label for="email">Email</label>
                <input v-model="email" id="email" type="text" placeholder="Email">
            </div>
            <div class="field">
                <label for="password">Password</label>
                <input v-model="password" id="password" type="text" placeholder="Password">
            </div>
            <button @click="register" class="ui button login-btn" type="submit">Register</button>
        </div>
    </form>
    
</template>

<script>
    /* eslint-disable no-alert, no-console */
    import axios from 'axios';

    export default {
        name: "Register",

        components: {

        },

        // props: [
        //     "firstName",
        //     "lastName",
        //     "email",
        //     "password"
        // ],

        data: function() {
            return {
                firstName: '',
                lastName: '',
                email: '',
                password:  ''
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

                axios.post("/api/register", form).then(response => {
                    console.log(response)
                }).catch(error => {
                    console.log(error);
                })
            },
            onSubmit: function() {
                
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>
