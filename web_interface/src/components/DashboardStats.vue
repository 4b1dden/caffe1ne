<script>
import { Bar } from 'vue-chartjs';

export default {
    extends: Bar,
    data() {
        return {
            options:  {
                responsive: true,
                maintainAspectRatio: false,
            }
        }
    },
    mounted () {
        this.renderChart(this.$store.getters.getDashboardStats, this.options);
    }
}
</script>