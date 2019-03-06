<template>
    <f7-block strong>
        <ul class="future-list">
            <li :key="index" v-for="(record, index) in records_future">
                <i>{{record.name}} si urobí {{record.amount}} 
                    {{record.amount < 5 ? dict2[record.intensity] : dict[record.intensity]}} 
                    káv{{record.amount < 5 ? "y" : ""}} o {{record.roastAt | moment("LT")}}</i>
            </li>
        </ul>
        <ul class="history-list">
            <li :key="index" v-for="(record, index) in records_past">
                <b>{{record.name}}</b> si spravil/-a <b>{{record.amount}} 
                    káv{{record.amount < 5 ? "y" : ""}} </b> ({{record.amount < 5 ? dict2[record.intensity] : dict[record.intensity]}}) o 
                    <i>{{record.roastAt | moment("LT")}}, {{record.roastAt | moment("l")}}</i>
            </li>
        </ul>
    </f7-block>
</template>

<script>
export default {
    props: ["records_past", "records_future"],
    data() {
        return {
            dict: {
                1: "slabých",
                2: "stredných",
                3: "silných"
            },
            dict2: {
                1: "slabé",
                2: "stredné",
                3: "silné"
            }
        }
    }
}
</script>