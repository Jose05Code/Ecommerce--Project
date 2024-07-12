<template>
  <nav :class="{fixed:isFixed , static:!isFixed}">
    <div class="nav-left none1">
      <button class="icon">
        <!-- ======SVG ICON====== -->
        <svg
          class="stroke"
          width="22"
          height="17"
          viewBox="0 0 19 14"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M1 1H17.5"
            stroke="#999999"
            stroke-width="1.71429"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M1 7H17.5"
            stroke="#999999"
            stroke-width="1.71429"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M1 13H17.5"
            stroke="#999999"
            stroke-width="1.71429"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>
      <button class="icon">
        <!-- ======SVG ICON====== -->
        <svg
          width="23"
          height="22"
          viewBox="0 0 19 18"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M8.18851 15.8761C3.67156 15.8761 0 12.3518 0 8.02636C0 3.70098 3.67156 0.171875 8.18851 0.171875C12.7055 0.171875 16.377 3.69155 16.377 8.02165C16.377 12.3518 12.7055 15.8714 8.18851 15.8714V15.8761ZM8.18851 1.59011C4.48746 1.59011 1.47452 4.47841 1.47452 8.02636C1.47452 11.5743 4.48746 14.4626 8.18851 14.4626C11.8896 14.4626 14.9025 11.5743 14.9025 8.02636C14.9025 4.47841 11.8896 1.59011 8.18851 1.59011Z"
            fill="#999999"
          />
          <path
            d="M17.9029 17.8268C17.7162 17.8268 17.5245 17.7561 17.3819 17.6195L13.3073 13.7134C13.0173 13.4354 13.0173 12.9878 13.3073 12.7145C13.5973 12.4413 14.0643 12.4366 14.3493 12.7145L18.4239 16.6206C18.7139 16.8986 18.7139 17.3462 18.4239 17.6195C18.2814 17.7561 18.0897 17.8268 17.9029 17.8268Z"
            fill="#999999"
          />
        </svg>
      </button>
    </div>
    <div class="logo">
      <img class="logo-img" src="../assets/images/logo.png" alt="logo" />
      <img class="logo-img-text" src="../assets/images/text_logo.png" alt="logo" />
    </div>
    <div class="nav-desktop-options none">
      <RouterLink to="">Inicio</RouterLink>
      <RouterLink to="">Catálogo</RouterLink>
      <RouterLink to="">Talleres</RouterLink>
      <RouterLink to="">Sobre Nosotros</RouterLink>
    </div>
    <div class="nav-right">
      <button class="none">
        <!-- ======SVG ICON====== -->
        <svg
          width="23"
          height="22"
          viewBox="0 0 19 18"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M8.18851 15.8761C3.67156 15.8761 0 12.3518 0 8.02636C0 3.70098 3.67156 0.171875 8.18851 0.171875C12.7055 0.171875 16.377 3.69155 16.377 8.02165C16.377 12.3518 12.7055 15.8714 8.18851 15.8714V15.8761ZM8.18851 1.59011C4.48746 1.59011 1.47452 4.47841 1.47452 8.02636C1.47452 11.5743 4.48746 14.4626 8.18851 14.4626C11.8896 14.4626 14.9025 11.5743 14.9025 8.02636C14.9025 4.47841 11.8896 1.59011 8.18851 1.59011Z"
            fill="#999999"
          />
          <path
            d="M17.9029 17.8268C17.7162 17.8268 17.5245 17.7561 17.3819 17.6195L13.3073 13.7134C13.0173 13.4354 13.0173 12.9878 13.3073 12.7145C13.5973 12.4413 14.0643 12.4366 14.3493 12.7145L18.4239 16.6206C18.7139 16.8986 18.7139 17.3462 18.4239 17.6195C18.2814 17.7561 18.0897 17.8268 17.9029 17.8268Z"
            fill="#999999"
          />
        </svg>
      </button>
      <img src="" alt="" />
      <RouterLink class="login border">
        <!-- ======SVG ICON====== -->
        <svg
          width="20"
          height="21"
          viewBox="0 0 17 18"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M16.362 17.9996C16.0804 17.9996 15.8501 17.7769 15.8501 17.5048V15.0405C15.8501 13.4966 14.5497 12.2397 12.9524 12.2397H3.92155C2.32426 12.2397 1.02391 13.4966 1.02391 15.0405V17.5048C1.02391 17.7769 0.793527 17.9996 0.511953 17.9996C0.230379 17.9996 0 17.7769 0 17.5048V15.0405C0 12.9522 1.76111 11.25 3.92155 11.25H12.9524C15.1128 11.25 16.874 12.9522 16.874 15.0405V17.5048C16.874 17.7769 16.6436 17.9996 16.362 17.9996Z"
            fill="#999999"
          />
          <path
            d="M8.43726 7.87452C6.26515 7.87452 4.5 6.10938 4.5 3.93726C4.5 1.76514 6.26515 0 8.43726 0C10.6094 0 12.3745 1.76514 12.3745 3.93726C12.3745 6.10938 10.6094 7.87452 8.43726 7.87452ZM8.43726 0.946457C6.79043 0.946457 5.44646 2.28569 5.44646 3.93726C5.44646 5.58883 6.79043 6.92806 8.43726 6.92806C10.0841 6.92806 11.4281 5.58883 11.4281 3.93726C11.4281 2.28569 10.0888 0.946457 8.43726 0.946457Z"
            fill="#999999"
          />
        </svg>

        <p class="none">Iniciar sesión</p>
      </RouterLink>
      <button class="carrito">
        <!-- ======SVG ICON====== -->
        <svg
          width="42"
          height="25"
          viewBox="0 0 26 19"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M13.0445 13.4968H6.96787C6.79042 13.4968 6.63663 13.3824 6.58931 13.2185L3.52534 2.69609H0.394333C0.17745 2.69609 0 2.52453 0 2.31484C0 2.10515 0.17745 1.93359 0.394333 1.93359H3.82504C4.00249 1.93359 4.15627 2.04797 4.20359 2.2119L7.26757 12.7343H13.0445C13.2614 12.7343 13.4389 12.9059 13.4389 13.1156C13.4389 13.3253 13.2614 13.4968 13.0445 13.4968Z"
            fill="#999999"
          />
          <path
            d="M14.2429 10.9902H6.23795C6.02107 10.9902 5.84362 10.8187 5.84362 10.609C5.84362 10.3993 6.02107 10.2277 6.23795 10.2277H13.9472L15.3747 5.32109H4.58965C4.37276 5.32109 4.19531 5.14953 4.19531 4.93984C4.19531 4.73016 4.37276 4.55859 4.58965 4.55859H15.8952C16.0174 4.55859 16.1357 4.61578 16.2106 4.71109C16.2856 4.8064 16.3092 4.9284 16.2777 5.04278L14.6294 10.7119C14.582 10.8759 14.4283 10.9902 14.2508 10.9902H14.2429Z"
            fill="#999999"
          />
          <path
            d="M7.52713 16.1998C7.97359 16.1998 8.33552 15.8499 8.33552 15.4183C8.33552 14.9866 7.97359 14.6367 7.52713 14.6367C7.08067 14.6367 6.71875 14.9866 6.71875 15.4183C6.71875 15.8499 7.08067 16.1998 7.52713 16.1998Z"
            fill="#999999"
          />
          <path
            d="M12.2303 16.1998C12.6767 16.1998 13.0386 15.8499 13.0386 15.4183C13.0386 14.9866 12.6767 14.6367 12.2303 14.6367C11.7838 14.6367 11.4219 14.9866 11.4219 15.4183C11.4219 15.8499 11.7838 16.1998 12.2303 16.1998Z"
            fill="#999999"
          />
        </svg>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { RouterLink } from 'vue-router'

let isFixed = ref(false);

const handleScroll = () => {
  isFixed.value = window.scrollY > 0;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
nav {
  z-index: 9999;
  width: 100%;
  background-color: #141414;
  display: flex;
  align-items: center;
  height: 60px;
  padding: 0 30px;
}
.fixed{
  position: fixed;
}
.static{
  position: static;
}
.nav-desktop-options {
  display: flex;
  justify-content: center;
  gap: 25px;
}
.nav-desktop-options a {
  text-decoration: none;
  border-bottom: 3px solid #99999900;
  transition: 0.2s ease;
}
.nav-desktop-options a:hover {
  flex-grow: 1;
  color: #427235;
  text-decoration: none;
  border-bottom: 3px solid #427235;
}
a,
p {
  text-decoration: none;
  color: #999999;
  font-family: 'Rubik';
  font-size: 19px;
}
.logo {
  flex-grow: 1;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}
.logo img {
  height: min-content;
}
.logo-img-text {
  width: 100px;
}
.logo-img {
  width: 60px;
}
button {
  background: none;
  border: none;
}
.nav-left {
  flex-grow: 1;
  display: flex;
  gap: 16px;
}
.nav-right {
  display: flex;
  justify-content: end;
  align-items: center;
  flex-grow: 1;
  display: flex;
}
.login {
  display: flex;
  gap: 8px;
  display: flex;
  align-items: center;
  height: 40px;
}
.border {
  margin: 0 15px;
}
.carrito{
  transform: translateY(2px);
}
button:hover{
  cursor: pointer;
}
button:hover .stroke path {
  stroke: #427235;
}
button:hover svg path {
  fill: #427235;
}
svg path {
  transition: 0.2s ease;
}
p {
  transition: 0.2s ease;
}
a:hover svg path {
  fill: #427235;
}
.login:hover p {
  color: #427235;
}
.none {
  display: none;
}
/* ==========RESPONSIVE========== */
@media (min-width: 1000px) {
  .none {
    display: flex;
  }
  .none1{
    display: none;
  }
  .border {
    border-right: 2px solid #427235;
    border-left: 2px solid #427235;
    padding: 0 20px;
    margin: 0 15px;
  }
  .logo{
    justify-content: start;
  }
}
</style>
