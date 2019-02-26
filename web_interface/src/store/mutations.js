export default {
    changeUserNickname: (state, payload) => {
        state.userNickname = payload;
    },
    setDashboardStats: (state, stats) => {
        state.stats.dashboard = stats;
    },
    setFullStats: (state, stats) => {
        state.stats.full = stats;
    }
}