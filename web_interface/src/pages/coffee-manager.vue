<template>
    <div>
        <f7-button fill @click="showNewCoffeeRequest = !showNewCoffeeRequest" class="col" round>{{!showNewCoffeeRequest ? "Nová káva?" : "Skry menu"}} </f7-button>
        <new-coffee-request v-if="showNewCoffeeRequest" />
        <f7-button fill @click="showCoffeeHistory = !showCoffeeHistory" class="col menu-btn" round>{{!showCoffeeHistory ? "Ukáž" : "Skry"}} krátku históriu</f7-button>
        <coffee-history v-if="showCoffeeHistory" />
    </div>
</template>

<script>
import NewCoffeeRequest from '../components/NewCoffeeRequest.vue';
import CoffeeHistory from '../components/CoffeeHistory.vue';

export default {
    data() {
        return {
            showNewCoffeeRequest: true,
            showCoffeeHistory: false
        }
    },
    components: {
        'new-coffee-request': NewCoffeeRequest,
        'coffee-history': CoffeeHistory
    }
}
</script>

<style>
.menu-btn {
    margin-top: 15px;
}
</style>
