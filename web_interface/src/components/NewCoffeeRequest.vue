<template>
    <f7-list form>
        <f7-list-input
        label="Meno"
        type="text"
        placeholder="Name"
        v-model="form.name"
        @input='form.name = $event.target.value'
        disabled
        />
        <f7-list-input 
        label="Počet káv"
        type="number"
        placeholder="amount"
        v-model='form.amount'
        @input="form.amount = parseInt($event.target.value)"
        min="2"
        max="10"
        step="2"
        />
        <f7-list-input
        label="Sila kávy"
        type="select"
        defaultValue="Slabá"
        v-model="form.intensity"
        @input="form.intensity = parseInt($event.target.value)"
        >
            <option :value="1">Slabá</option>
            <option :value="2">Stredná</option>
            <option :value="3">Silná</option>
        </f7-list-input>
        <f7-block-title>Kedy?</f7-block-title>
        <f7-list>
            <f7-list-item @change="form.roastRightAway = true" value="true" radio :checked="form.roastRightAway" name="radio1" title="Hneď" v-model="form.roastRightAway"/>
            <f7-list-item @change="form.roastRightAway = false" value="false" radio name="radio1" title="Zvolím si čas" v-model="form.roastRightAway"/>
        </f7-list>
        
        <div class="schedule-later" v-if="!form.roastRightAway">
            o <input class="schedule-input" type="number" v-model="form.delayHours" min="0" max="4" @input="form.delayHours = parseInt($event.target.value)"> 
            hodín a 
            <input class="schedule-input" type="number" v-model="form.delayMinutes" min="1" max="59" @input="form.delayMinutes = parseInt($event.target.value)">
            minút
        </div>
        <f7-button @click="onButtonClick" class="col" round>Zrob kaveju</f7-button>
    </f7-list>
</template>

<script>
import CoffeeService from '../services/CoffeeService.js';

export default {
    data() {
        return {
            form: {
                name: this.$store.getters.getUserNickname,
                amount: 2,
                intensity: 1,
                roastRightAway: true,
                delayHours: 0,
                delayMinutes: 30
            }
        }
    },
    methods: {
        onButtonClick: function() {
            CoffeeService.requestCoffee(this.form).then(response => {
                console.log(response);
            })
        }
    }
}
</script>

<style>
    .schedule-input {
        display: inline-block !important;
        width: 20% !important;
    }
</style>