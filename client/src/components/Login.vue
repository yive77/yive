
<template>
    <form v-on:submit.prevent="onSubmit" class="ui form main-form">
        <div class="form-inner">
            <div class="field">
                <label for="login-email">Email</label>
                <input v-model="email" id="login-email" type="text" name="email" placeholder="Email">
            </div>
            <div class="field">
                <label for="password">Password</label>
                <input v-model="password" id="password" type="text" name="Password" placeholder="Password">
            </div>
            
            <button class="ui button login-btn" type="submit">Login</button>
        </div>
    </form>
</template>

<script>

    import {mapActions, mapGetters} from 'vuex';
    import qs from 'querystring';

    const login_url = "http://localhost:8081/api/login";

    export default {
        name: "Login",
        data: () => {
            return { 
                email: '',
                password: ''
            }
        },
        methods: {
            login: () => {
                let form = {
                    email: this.email.trim(),
                    password: this.password.trim(),
                }

                if (form.email.length > 0 && form.password.length > 0) {
                    axios.post(login_url, qs.stringify(form)).then(response => {
                        console.log(response);
                    }).catch(error => {
                        console.log(error);
                    })
                }
            },
            onSubmit: () => {}
        },
        computed: {
            ...mapGetters(['isAuthorized'])
        }
    }
</script>

<style lang="scss">
    .main-form {
        @extend .main-form;
    }
</style>
