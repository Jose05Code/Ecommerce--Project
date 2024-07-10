<template>
<NavBarComp/>
<slot/>
<FooterComp/>
</template>

<script setup>
    import NavBarComp from '@/components/NavBarComp.vue';
    import FooterComp from '@/components/FooterComp.vue';
</script>

<style scoped>
    
</style>