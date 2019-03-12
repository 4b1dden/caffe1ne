<template>
  <f7-page>
    <f7-navbar title="Nastavenia" back-link="Back"></f7-navbar>
    <f7-block-title>Obecné nastavenia</f7-block-title>
    <f7-row>
        <f7-col width="50">
            <gen-settings />
        </f7-col>
        <f7-col width="50">
            YOOOOOOOo
        </f7-col>
    </f7-row>
  </f7-page>
</template>

<script>
import GeneralSettings from '../components/GeneralSettings.vue';

export default {
    components: {
        'gen-settings': GeneralSettings
    },
}
</script>

<style scoped>
.list {
    margin: 0;
}
</style>