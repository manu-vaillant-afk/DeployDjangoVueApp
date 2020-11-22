<template>
  <div class="nav-bar">
    <nav class="">
      <div class="navitem">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item" v-if="accessToken!=null"><router-link :to = "{ name:'logout' }">Logout</router-link></li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  export default {
    name: 'Navbar',
    computed: mapState(['accessToken'])
  }
</script>

<style lang="scss">
$maincolor:#3B3B98;
$textcolor:#fff;

.nav-bar{
  margin: 0;
  padding: 1em;
  background-color: $maincolor;
  font-family: "Gill Sans", sans-serif;
  
  ul{
    margin: 0;
    list-style-type: none;
  }

  a {
    color: $textcolor;
    text-decoration: none;
    margin-left: auto;
  }
}
</style>