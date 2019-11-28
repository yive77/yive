
<template>
    <form v-on:submit.prevent="onSubmit" class="ui form main-form">
        <div class="form-inner">
            <div class="form-error">{{ form_error }}</div>
            <div class="field">
                <label for="login-email">Email</label>
                <input v-model="email" id="login-email" type="text" name="email" placeholder="Email">
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


    
    
    export default {
        name: "Login",
        data: () => {
            return { 
                email: '',
                password: '',
                form_error: '',
                login_url: '',
            }
        },
        methods: {
            login: function() {
                let form = {
                    email: this.email.trim(),
                    password: this.password.trim(),
                }
                let self = this;
                this.$store.dispatch('login', form).then(response => {
                    if (response.data.error)
                        self.form_error = response.data.message;
                    else if (response.data.success) {
                        self.$router.push('/profile');
                    }
                }).catch(err => {
                    console.log(err);
                    self.form_error = "All fields are required";
                })
            },
            onSubmit: () => {}
        },
        computed: {
            isAuthorized: function() {
                return this.$store.getters.isAuthorized;
            }
        }
    }
</script>

<style lang="scss">
    .main-form {
        @extend .main-form;
    }
</style>
