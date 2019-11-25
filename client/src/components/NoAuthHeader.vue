<template>
    <div class="">
        <nav class="navbar navbar-expand-lg">
          <a class="navbar-brand" href="/">Yive Platform</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fa fa-user"></i>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link login" :class="{ active: activeTab === 'login' }" @click="$router.push('/login')">Login</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link register" @click="$router.push('/register')">Register</a>
                </li>
              <!-- <li class="nav-item dropdown"> -->
                <!-- <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Dropdown
                </a> -->
                <!-- <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <a class="dropdown-item" href="#">Action</a>
                  <a class="dropdown-item" href="#">Another action</a>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="#">Something else here</a>
                </div> -->
              <!-- </li> -->
              <!-- <li class="nav-item">
                <a class="nav-link disabled" href="#">Disabled</a>
              </li> -->
            </ul>
            <!-- <form class="form-inline my-2 my-lg-0">
                <a href="#">
                    <span>Login</span>
                </a>
                <a href="#">
                    <span>Register</span>
                </a>
            </form> -->
          </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "NoAuthHeader"
    }
</script>

<style lang="scss">
nav {
    box-shadow: $box-shadow;
    background: $bg-primary;
    .navbar-brand {
        color: $fg-primary !important;
    }
    .navbar-toggler {
        background: $fg-primary;
        color: $bg-primary;
        height: 40px;
    }
    .nav-link {
        padding-left: 10px !important;
        color: $fg-primary !important;
    }
    .login {
        .active {
            background: $fg-primary;
            color: $bg-primary;
        }
        &:hover {
            @extend .link-hover;
        }
    }
    .register {
        &:hover {
            @extend .link-hover;
        }
    }
}

</style>
