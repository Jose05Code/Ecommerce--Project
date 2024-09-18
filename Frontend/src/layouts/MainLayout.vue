<template>
<NavBarComp/>
<slot/>
<FooterComp/>
</template>

<script setup>
    import NavBarComp from '@/components/layoutComponents/NavBarComp.vue';
    import FooterComp from '@/components/layoutComponents/FooterComp.vue';
</script>

<style scoped>
    
</style>