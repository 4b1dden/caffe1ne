export default {
    getUserNickname: (state) => {
        return state.userNickname
    },
    getDashboardStats: (state) => {
        return state.stats.dashboard
    },
    getSidebarStatsPast: (state) => {
        let now = new Date();
        let iter = 0;
        while (new Date(state.stats.all[iter].roastAt) > now) iter++;

        return state.stats.all && state.stats.all.length > 0 ? state.stats.all.slice(iter, iter+10) : []
    },
    getCoffeesToBeMade: (state) => (shouldSplice) => {
        let data = state.stats.all.filter(stat => {
            return new Date(stat.roastAt) > new Date()
        });
        return shouldSplice ? data.splice(0,3) : data;
    },
    getAllMadeCoffees: (state) => {
        return state.stats.all;
    }
}