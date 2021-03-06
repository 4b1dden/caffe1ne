export default {
    setUserName: (state, payload) => {
        if (typeof payload == "string") state.user.name = payload;
    },
    setDashboardStats: (state, stats) => {
        state.stats.dashboard = stats;
    },
    setAlltimeStats: (state, stats) => {
        state.stats.all = stats;
    },
    addNewCoffeeToDashboardStats: (state, form) => {
        let willBeRoastedAt = new Date();
 
        if (form.roastRightAway) {
            state.stats.dashboard.datasets[0].data[6] += form.amount;
        }
    }
}