<template>
    <div class="">
        <NoAuthHeader></NoAuthHeader>
        <div class="jumbotron jumbotron-fluid">
            <div class="container">
                <h1>Digital Identity Verification</h1>
                <p>Save time, money, and everything else.</p>
            </div>
        </div>
    </div>
</template>

<script>
    import NoAuthHeader from './NoAuthHeader'

    export default {
        name: "Home",
        components: {
            NoAuthHeader
        }
    }

</script>

<style lang="scss">

</style>
