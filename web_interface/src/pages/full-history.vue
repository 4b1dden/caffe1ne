<template>
  <f7-page>
    <f7-navbar title="História" back-link="Back"></f7-navbar>
    <f7-block-title>Celková história urobených káv</f7-block-title>
    <coffee-stats-list :records_future="records_future" :records_past="records_past" />
  </f7-page>
</template>

<script>
import CoffeeStatsList from '../components/CoffeeStatsList.vue';

export default {
    components: {
        'coffee-stats-list': CoffeeStatsList,
    },
    computed: {
        records_future() {
            return this.$store.getters.getCoffeesToBeMade(false);
        },
        records_past() {
            return this.$store.getters.getAllMadeCoffees;
        }
    }
}
</script>