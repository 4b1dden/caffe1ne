import CoffeeService from '../services/CoffeeService.js';

export default {
    fetchAllStats({ commit }) {
        return new Promise (
            function (resolve, reject) {
                CoffeeService.getCoffeeStats().then(data => {
                    // todo :separate all stats from the dashboard ones
                    commit("setAlltimeStats", data.all);
                    commit("setDashboardStats", data.dashboard);
                    resolve();
                }).catch(err => {
                    console.log(err);
                });
            }
        )
    }
}