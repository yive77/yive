<template>
    <div class="height-full">
        <NoAuthHeader :tab="login"></NoAuthHeader>
        <LoginForm></LoginForm>
    </div>
</template>

<script>
    import NoAuthHeader from './NoAuthHeader'
    import LoginForm from './LoginForm'

    export default {
        name: 'Login',
        components: {
            NoAuthHeader,
            LoginForm
        }
    }
</script>

<style lang="scss">

</style>
