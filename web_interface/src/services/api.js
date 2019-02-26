import { create } from 'apisauce'
import constants from '../constants';

export default create({
    baseURL: constants.API.DEFAULT,
    // headers: { Accept: 'application/vnd.github.v3+json' },   
})