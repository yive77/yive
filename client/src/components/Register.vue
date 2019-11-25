<template>
    <div class="height-full">
        <NoAuthHeader></NoAuthHeader>
        <div class="register-container">
            <form>
                <div class="form-group">
                    <label for="register-email">Email address</label>
                    <input type="email" class="form-control" id="register-email" aria-describedby="emailHelp" placeholder="Enter email">
                    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                </div>
                <div class="form-group">
                    <label for="register-password">Password</label>
                    <input type="password" class="form-control" id="register-password" placeholder="Password">
                </div>
                <div class="text-center width-full">Or</div>
                <div class="social-buttons">
                    <a class="btn btn-social btn-facebook">
                        <i class="fa fa-2x fa-facebook"></i>

                    </a>

                    <a class="btn btn-social btn-google">
                        <i class="fa fa-2x fa-google"></i>
                    </a>
                </div>
                <!-- <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1">
                    <label class="form-check-label" for="exampleCheck1">Check me out</label>
                </div> -->
                <button type="submit" class="btn btn-primary form-control">Register</button>

            </form>
        </div>
    </div>
</template>

<script>
    import NoAuthHeader from './NoAuthHeader'
    export default {
        name: "Register",
        components: {
            NoAuthHeader,
        },
        
    }
</script>

<style lang="scss">
    .register-container {
        display: flex;
        align-items: center;
        height: calc(100% - #{$navbar-height});
        form {
            width: 50%;
            margin: 0 auto;
            padding: 40px;
            box-shadow: $box-shadow;
        }
    }
</style>
