<template>
  <MainLayout> 
    <HeaderHomeComp/>
    <ItemsComp/>
    <AboutUsComp/>
  </MainLayout>
</template>

<script setup>
import MainLayout from '@/layouts/MainLayout.vue'
import HeaderHomeComp from '@/components/homeComponents/HeaderHomeComp.vue';
import ItemsComp from '@/components/homeComponents/ItemsComp.vue';
import AboutUsComp from  '@/components/homeComponents/AboutUsComp.vue';
</script>

<style scoped></style>
