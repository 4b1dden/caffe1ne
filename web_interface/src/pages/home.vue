<template>
  <f7-page>
    <f7-navbar>
      <f7-nav-right>
        <f7-link icon-if-ios="f7:settings" icon-if-md="material:settings" @click="onClick"></f7-link>
      </f7-nav-right>
      <f7-nav-title>caffe1ne // ovládací panel</f7-nav-title>
    </f7-navbar>
    <f7-block>
      <f7-row>
        <f7-col width="60">
          <stats-manager />
        </f7-col>
        <f7-col width="40">
          <coffee-manager />
        </f7-col>
      </f7-row>
    </f7-block>
  </f7-page>
</template>
<script>
import CoffeeManager from './coffee-manager.vue';
import StatsManager from './stats-manager.vue';
import CoffeeService from '../services/CoffeeService.js';

export default {
    data() {
      return {
        isLoading: true
      }
    },
    components: {
      'coffee-manager': CoffeeManager,
      'stats-manager': StatsManager
    }, 
    methods: {
      onClick: function () {
        this.$f7router.navigate("/settings/");
      }
    }
}
</script>
