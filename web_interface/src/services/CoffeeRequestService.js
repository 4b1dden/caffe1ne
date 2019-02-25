import api from './api';
import constants from '../constants';

export default {
    getAllCoffeeRequests: function() {
        return new Promise (
            function (resolve, reject) {
                api.get(constants.API.ENDPOINTS.COFFEE.ENTRY)
                .then(response => {
                    if (response.ok) {
                        resolve(response.data);
                    } else {
                        reject(response);
                    }
                })
            }
        )
    }
}