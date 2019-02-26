<template>
    <div>
        <chart v-if="statsFetched" />
    </div>
</template>

<script>
import DashboardStats from '../components/DashboardStats.vue';

export default {
    components: {
        'chart': DashboardStats
    },
    data () {
        return {
            statsFetched: false,
        }
    },
    created() {
        let that = this;
        this.$store.dispatch("fetchDashboardStats").then(() => {
            that.statsFetched = true;
        });
    }
}
</script>