<template>

  <div class="center-item loginpage">
        
		<form @submit.prevent="login">
      <p v-if="incorrectAuth">Erreur de connexion</p>
			<input v-model="username" name="username" type="text" placeholder="Nom d'utilisateur">
			<input v-model="password" name="password" type="password" placeholder="Mot de passe">
			<button type="submit">Se connecter</button>
		</form>

	</div>
</template>

<script>
export default {
    name: 'Login',
    data () {
        return {
            username: '',
            password: '',
            incorrectAuth: false
        }
    },
    methods: {
        login() {
            this.$store.dispatch('userLogin', {
                username: this.username,
                password: this.password
            })
            .then(() => {
                this.$router.push({name : 'todos'})
            })
            .catch(err => {
                console.log("erreur")
                console.log(err)
                this.incorrectAuth = true
            } )
        }
    }
}
</script>

<style lang="scss">
$maincolor:#3B3B98;
$textcolor:#fff;
$font-family:Nunito Sans;

.loginpage {
  font-family: $font-family;
  background-color: $maincolor;
  margin: 0;
}

.center-item {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100vh;

  form {
    width: 40%;
    box-shadow: 1px 0 10px 15px rgba(0, 0, 0, .3);
    padding: 40px;
    background-color: #fff;

    input {
      width: 100%;
      box-sizing: border-box;
      margin-top: 20px;
      outline: none;
      border: none;
      background-color: #ecf0f1;
      padding: 10px;
      line-height: 2;
      font-size: 16px;
    }

    button {
      background-color: #4834d4;
      color: $textcolor;
      font-size: 18px;
      width: 100%;
      outline: none;
      border: none;
      padding: 15px;
      margin-top: 20px;
      cursor: pointer;

      &:hover {
        background-color: #686de0;
      }

    }

    p {
      text-align: center;
      margin-bottom: 0px;
      color: red;
     
    }
  }
}


</style>