<template>
  <div class="todos">
      <Navbar></Navbar>
      
        <div class="container todos" id="todos">
            <div class="todoForm center-addTodo my-4">
                <h2>Ajouter un todo :</h2>
                <form action="" method="post" @submit.prevent="submitForm">
                    <p v-if="error">
                        <b>Veuillez remplir le champ !</b>
                    </p>
                    <input placeholder="Tâche" id="todoValue" type="text" v-model="newTodoValue" name="newTodoValue">
                    <input class="button" type="submit" value="Ajouter">
                </form>
            </div>
            <div class="todo card" v-for="(todo, index) in APIData" :key="index" :class="{editing: todo.editing, checked: todo.checked}">
                <div class="card-body py-3 row">
                    <span class="todo-header ">
                        <a href="#" @click.prevent="checked(todo)">
                            <span class="btn btn-danger btn-sm mr-4 ml-2" v-if="todo.checked">
                                <img src="../assets/icon_uncheck.png" width="15px">
                            </span>
                            <span v-else class="btn btn-success btn-sm mr-4 ml-2">
                                <img src="../assets/icon_check.png" width="15px">
                            </span>
                        </a>

                    </span>
                    <div class="todo-body" @click="edit(todo)">
                        <div v-if="todo.checked">
                            <s> {{ todo.value }} </s>
                        </div>
                        <div v-else>
                            {{ todo.value }}
                        </div>
                        
                    </div>
                    <a class="btn btn-dark btn-sm mx-3 ml-auto" href="#" @click.prevent="del(todo)">
                            Supprimer
                    </a>
                    <input class="todo-body" type="text" @keyup.enter="doedit(todo)" v-model="todo.value">
                </div>
            </div>
        </div>

	</div>
</template>

<script>
    import Navbar from '../components/Navbar'
    import { getAPI } from '../axios-api'
    import { mapState } from 'vuex'

    export default {
        name : 'Todos',
        data() {
            return {
                // APIData: [],
                error: false,
                newTodoValue: null,
            }
        },
        components: {
            Navbar
        },
        computed: mapState(['APIData']),
        created() {
            // var token = this.$store.state.accessToken
            getAPI.get("/todos/", { headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}})
                .then(response => {
                    response.data.forEach(function(el){
                        el.editing = false
                    });  
                    this.$store.state.APIData = response.data
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)    
                })
        },
        methods: {
            checked(todo) {
                todo.checked = ! todo.checked
                getAPI.put(/todos/+todo.uuid+'/', 
                    {   
                        value: todo.value,
                        checked: todo.checked 
                    },
                    {
                        headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}
                    },
                );
            },
            del(todo) {
                this.APIData.splice(this.APIData.indexOf(todo), 1)
                getAPI.delete(/todos/+todo.uuid+'/',
                    {
                        headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}
                    },
                );
            },
            edit(todo) {
                todo.editing = true
            },
            doedit(todo) {
                todo.editing = false
                getAPI.put(/todos/+todo.uuid+'/', 
                    { 
                        value: todo.value,
                        checked: todo.checked 
                    },
                    {
                        headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}
                    },
                );
            },
            submitForm(){
                console.log("owner : "+this.$)
                if(! this.newTodoValue){
                    this.error = true
                    return
                }
                this.error = false
                getAPI.post('/todos/', 
                    {
                        value: this.newTodoValue,
                        checked: false
                    },
                    {
                        headers: {Authorization: 'Bearer ' + this.$store.state.accessToken}
                    },
                )
                .then(response => {
                    var newTodo = response.data
                    newTodo.editing = false
                    this.APIData.push(newTodo)
                    this.newTodoValue = null
                }) 
            },
        },   
    }

</script>

<style lang='scss'>
$maincolor:#3B3B98;
$textcolor:#fff;
$font-family: Helvetica;

.container {
    max-width: 1024px;
    margin: 0 auto;
    font-family:  $font-family;
}

.todoForm{
    margin-bottom: 1em;
    form {
        background-color: #fff;

        input {
            width: 100%;
            box-sizing: border-box;
            margin-top: 10px;
            border: none;
            background-color: #ecf0f1;
            padding: 10px;
            font-size: 16px;
        }

        .button {
            background-color: $maincolor;
            color: $textcolor;
            cursor: pointer;

                &:hover {
                    background-color: #686de0;
                }

            }
    }
}

.todos {
    margin-bottom: .5em; 
}

.todo {
    margin-bottom: .5em;
    position: relative;
}

.todo input.todo-body {
    display: none; 
}

.todo.editing div.todo-body {
    display: none; 
}

.todo.editing input.todo-body {
    display: block; 
}

.todo.checked {
    background-color: #c3c3c3d8;
}

.center-addTodo{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

</style>