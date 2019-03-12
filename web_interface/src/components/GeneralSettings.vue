<template>
      <f7-list form>
        <f7-list-input
        label="Meno"
        type="text"
        placeholder="Name"
        v-model="user.name"
        @input="user.name = $event.target.value"
        />

        <f7-button @click="saveUserInfo" class="col" round>Ulož údaje</f7-button>
    </f7-list>
</template>

<script>
export default {
    data() {
        return {
            user: {
                name: this.$store.getters.getUserName
            }
        }
    },
    methods: {
        saveUserInfo: function () {
            this.$store.dispatch("setUserData", this.user);
        }
    }
}
</script>

