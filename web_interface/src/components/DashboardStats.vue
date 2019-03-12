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
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                            callback: function (value) { if (Number.isInteger(value)) { return value; } },
                            stepSize: 1
                        }
                    }]
                }
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