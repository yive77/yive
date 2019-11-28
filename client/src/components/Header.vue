<template>
    <div class="ui secondary pointing menu header-style">
        
        <a href="/" class="item">Yive Platform</a>
        <a href="/" class="active item">Home</a>

        <div class="right menu auth">
            <div v-if="isAuthorized" class="right-menu-options">
                <a class="ui item" @click="$router.push('/profile')">Profile</a>
                <a class="ui item" @click="logout">Logout</a>
            </div>
            <div v-else class="right-menu-options">
                <a class="ui item" @click="$router.push('/login')">Login</a>
                <a class="ui item" @click="$router.push('/register')">Register</a>
            </div>
        </div>
    </div>
</template>    

<script>
    /* eslint-disable no-alert, no-console */

    export default {
        name: "Header",

        methods: {
            logout: function() {
                this.$store.dispatch('logout');
                this.$router.push('/login');
            }
        },
        computed: {
            isAuthorized: function() {
                return this.$store.getters.isAuthorized;
            },
        }
    }
</script>

<style lang="scss" scoped>
    .header-style {
        height: $navbar-height;

        .right-menu-options {
            display: inherit;
        }
    }
    
</style>
