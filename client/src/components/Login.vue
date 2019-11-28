
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

    export default {
        name: "Login",
        data: () => {
            return { 
                email: '',
                password: ''
            }
        },
        methods: {
            ...mapActions(['login']),
            onSubmit: () => {
}
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
