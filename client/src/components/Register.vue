<template>
    <NoAuthHeader :active-tab="register"></NoAuthHeader>
</template>

<script>
    import NoAuthHeader from './NoAuthHeader'

    export default {
        name: "Register",
        components: {
            NoAuthHeader
        }
    }
</script>

<style>

</style>
