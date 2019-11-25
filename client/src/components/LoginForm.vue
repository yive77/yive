<template>
    <div class="login-container">
        <form>
            <div class="form-group">
                <label for="login-email">Email address</label>
                <input type="email" class="form-control" id="login-email" aria-describedby="emailHelp" placeholder="Enter email">
                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
            </div>
            <div class="form-group">
                <label for="login-password">Password</label>
                <input type="password" class="form-control" id="login-password" placeholder="Password">
            </div>
            <!-- <div class="form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div> -->
            <button @click="login" type="submit" class="btn btn-primary form-control">Submit</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: "LoginForm",
        methods: {
            login: function() {
                console.log("logging in");
            }
        }
    }
</script>

<style lang="scss" scoped>

.login-container {
    display: flex;
    align-items: center;
    height: calc(100% - #{$navbar-height});
    width: 50%;
    margin: 0 auto;

    form {
        box-shadow: $box-shadow !important;
        width: 100%;
        padding: 40px;
    }
}

</style>
