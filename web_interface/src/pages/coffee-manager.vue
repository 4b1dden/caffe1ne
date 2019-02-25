<template>
    <div>
        <f7-button fill @click="showNewCoffeeRequest = !showNewCoffeeRequest" class="col" round>{{!showNewCoffeeRequest ? "Nová káva?" : "Skry menu"}} </f7-button>
        <new-coffee-request v-if="showNewCoffeeRequest" />
        <!-- <f7-button fill @click="showCoffeeHistory = !showCoffeeHistory" class="col" round>{{!showCoffeeHistory ? "Ukáž" : "Skry"}} krátku históriu</f7-button> -->
    </div>
</template>

<script>
import NewCoffeeRequest from '../components/NewCoffeeRequest.vue';

export default {
    data() {
        return {
            showNewCoffeeRequest: false,
            showCoffeeHistory: false
        }
    },
    mounted() {
        console.log(this.$store.state.testProperty)
    },
    components: {
        'new-coffee-request': NewCoffeeRequest
    }
}
</script>