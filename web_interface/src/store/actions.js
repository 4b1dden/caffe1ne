import CoffeeService from '../services/CoffeeService.js';

export default {
    fetchDashboardStats({ commit }) {
        return new Promise (
            function (resolve, reject) {
                CoffeeService.getCoffeeStats("dashboard").then(data => {
                    // todo :separate all stats from the dashboard ones
                    console.log(data)
                    commit("setDashboardStats", data);
                    resolve();
                }).catch(err => {
                    console.log(err);
                });
            }
        )
    }
}