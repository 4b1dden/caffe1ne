<template>
    <div>
        <coffee-stats-list :records_future="records_future" :records_past="records_past" />
        <f7-button @click="onButtonClick" class="col" round>Ukáž všetku históriu</f7-button>
    </div>
</template>

<script>
import CoffeeStatsList from './CoffeeStatsList.vue';

export default {
    components:{ 
        'coffee-stats-list': CoffeeStatsList
    },
    methods: {
        onButtonClick() {
            this.$f7router.navigate('/full-history/');
        }
    },
    computed: {
        records_past() {
            return this.$store.getters.getSidebarStatsPast;
        },
        records_future() {
            return this.$store.getters.getCoffeesToBeMade(true);
        }
    }
}
</script>