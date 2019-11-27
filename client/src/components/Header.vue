<template>
    <div class="ui secondary pointing menu header-style">
        
        <a href="/" class="item">Yive Platform</a>
        <a href="/" class="active item">Home</a>

        <div class="right menu auth">
            <div v-if="isAuthorized" class="right-menu-options">
                <a class="ui item" @click="$router.push('/profile')">Profile</a>
                <a class="ui item" @click="$router.push('/logout')">Logout</a>
            </div>
            <div v-else class="right-menu-options">
                <a class="ui item" @click="$router.push('/login')">Login</a>
                <a class="ui item" @click="$router.push('/register')">Register</a>
            </div>
        </div>
    </div>
</template>    

<script>

    import {mapActions, mapGetters} from 'vuex';

    export default {
        name: "Header",
        methods: {
            ...mapActions(['login'])
        },
        computed: {
            ...mapGetters(['isAuthorized'])
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
