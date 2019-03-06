<script>
import { Bar } from 'vue-chartjs';

export default {
    extends: Bar,
    data() {
        return {
            _chart: null,
            options:  {
                responsive: true,
                maintainAspectRatio: false,
            }
        }
    },
    methods: {
        drawChart() {
            this.renderChart(this.chartData, this.options);
        }
    },
    computed: {
        chartData: function () {
            return this.$store.getters.getDashboardStats;
        }
    },
    mounted () {
        this.drawChart();
    },
    watch: {
        chartData() {
            this.drawChart();
        }
    }
}
</script>