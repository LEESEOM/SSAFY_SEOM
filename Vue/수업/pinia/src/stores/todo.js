import { defineStore } from "pinia";
import { ref, computed } from 'vue'

export const useTodoStore = defineStore('todo', () => {

  const todos = ref([])

  const completedTodos = computed(()=>{
    return todos.value.filter((todo)=>{
      return todo.isCompleted
    })
  })

  function addTodo(todo) {
    todos.value.push(todo)
  }

  return { todos, completedTodos, addTodo }
})