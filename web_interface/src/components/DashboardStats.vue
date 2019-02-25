<script>
import { Bar } from 'vue-chartjs';

let options = {
    responsive: true,
    maintainAspectRatio: false,
}

// example data
let data = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
        {
          label: 'fess data',
          backgroundColor: '#f87979',
          data: [40, 39, 10, 40, 39, 80, 40]
        }
    ]
};

export default {
    extends: Bar,
    mounted () {
        this.renderChart(data, options);
    }
}
</script>